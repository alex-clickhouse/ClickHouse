import json
import re
import sys
import traceback
from dataclasses import dataclass
from typing import List, Optional, Tuple

sys.path.append("./")

from ci.praktika.gh import GH
from ci.praktika.result import Result
from ci.praktika.utils import Shell


class CheckStatuses:
    PR = "PR"
    CH_INC_SYNC = "CH Inc sync"
    MERGEABLE_CHECK = "Mergeable Check"


FORCE_MERGE = True


@dataclass
class CommitStatus:
    state: str
    description: str
    url: str
    context: str


report_url = None


class UserSelector:
    def get_user_choice_from_menu(menuitems, question="Enter your choice"):
        menu_map = {}
        for i, item in enumerate(menuitems, start=1):
            menu_map[i] = item
            val = item[0] if isinstance(item, tuple) else item
            print(f"{i}. {val}")

        while True:
            try:
                choice = input(f"\n{question} (1-{len(menuitems)}): ")
                choice_num = int(choice)

                if 1 <= choice_num <= len(menuitems):
                    selected_item = menu_map[choice_num]
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\n\nSelection cancelled.")
                return

        return selected_item

    def get_user_numeric_input(question="Enter a number", validator=lambda x: True):
        while True:
            try:
                choice = input(f"\n{question}: ")
                choice_num = int(choice)
                if validator(choice_num):
                    break
                else:
                    raise ValueError("Invalid input. Please enter a number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyboardInterrupt:
                print("\n\nSelection cancelled.")
                return
        return choice_num

    def get_yes_or_no_answer(question="Do you want to proceed?"):
        while True:
            try:
                choice = input(f"\n{question} (y/n): ")
                if choice.lower() in ("y", "yes"):
                    return True
                elif choice.lower() in ("n", "no"):
                    return False
                else:
                    print("Invalid choice. Please enter 'y' or 'n'.")
            except KeyboardInterrupt:
                print("\n\nSelection cancelled.")
                return

    def get_user_string_input(question, validator=lambda x: True):
        while True:
            try:
                choice = input(f"\n{question}: ")
                if validator(choice):
                    break
                else:
                    raise ValueError("Invalid input. Please enter a string.")
            except ValueError:
                print("Invalid input. Please enter a string.")
            except KeyboardInterrupt:
                print("\n\nSelection cancelled.")
                return
        return choice


@dataclass
class CIGHIssue:
    title: str
    url: str
    labels: List[str]


class JobTypes:
    STATELESS = "Stateless"
    INTEGRATION = "Integration"
    AST_FUZZER = "AST Fuzzer"
    BUILD = "Build"
    FORMATTER = "Formatter"
    BUZZ_FUZZER = "Buzz"
    DOCKER = "Docker"
    COMPATIBILITY = "Compatibility"
    STRESS = "Stress"
    UPGRADE = "Upgrade"
    PERFORMANCE = "Performance"
    FINISH_WORKFLOW = "Finish Workflow"


@dataclass
class CIFailure:
    job_name: str
    job_status: str
    test_name: str
    test_status: str
    test_info: str
    praktika_result: Result
    issue: Optional[CIGHIssue] = None
    job_type: str = ""
    ignorable: bool = False

    def __post_init__(self):
        if "Stateless" in self.job_name:
            self.job_type = JobTypes.STATELESS
            if (
                any(
                    t in self.test_name
                    for t in ["Scraping", "Killed", "Fatal messages", "Server died"]
                )
                or self.test_status == "SERVER_DIED"
            ):
                # TODO: Find right way to handle this
                self.ignorable = True
                self.praktika_result.set_comment("IGNORED")
        elif "Integration" in self.job_name:
            self.job_type = JobTypes.INTEGRATION
        elif "AST" in self.job_name:
            self.job_type = JobTypes.AST_FUZZER
        elif "formatter" in self.job_name:
            self.job_type = JobTypes.FORMATTER
            self.ignorable = True
        elif "Buzz" in self.job_name:
            self.job_type = JobTypes.BUZZ_FUZZER
            self.ignorable = True
        elif "Build" in self.job_name:
            self.job_type = JobTypes.BUILD
        elif (
            "Docker server image" in self.job_name
            or "Docker keeper image" in self.job_name
        ):
            self.job_type = JobTypes.DOCKER
        elif "Compatibility check" in self.job_name:
            self.job_type = JobTypes.COMPATIBILITY
        elif "Stress" in self.job_name:
            self.job_type = JobTypes.STRESS
            self.ignorable = True
            self.praktika_result.set_comment("IGNORED")
        elif "Upgrade" in self.job_name:
            self.job_type = JobTypes.UPGRADE
        elif "Performance" in self.job_name:
            self.job_type = JobTypes.PERFORMANCE
        elif "Finish Workflow" in self.job_name:
            self.job_type = JobTypes.FINISH_WORKFLOW
        else:
            raise Exception(f"Unknown job type for job name: {self.job_name}")
        self.issue_url = self.praktika_result.get_hlabel_link("flaky") or ""
        self.labels = self.praktika_result.ext.get("labels", [])
        self.cidb_link = self.praktika_result.get_hlabel_link("cidb") or ""

    def __str__(self):
        return f"  {self.test_status or self.job_status}: {self.job_name}: {self.test_name if self.test_name else 'N/A'}. Flags: {', '.join(self.labels) or 'not flaged'}. Issue: {self.issue_url or 'not found'}"

    def __repr__(self):
        job_res = Result(
            name=self.job_name, status=self.job_status, results=[self.praktika_result]
        )
        res = job_res.to_stdout_formatted(
            truncate_from_top=False, max_info_lines_cnt=20, max_line_length=200
        )
        res += f"\n - flags: {', '.join(self.labels) or 'not flaged'}"
        res += f"\n - issue: {self.issue_url or 'not found'}"
        res += f"\n - cidb: {self.cidb_link or 'not found'}"
        return res

    @staticmethod
    def group_by_job(
        failures: List["CIFailure"],
    ) -> List[Tuple[str, List["CIFailure"]]]:
        grouped = {}
        for failure in failures:
            if failure.job_name not in grouped:
                grouped[failure.job_name] = []
            grouped[failure.job_name].append(failure)
        return list(grouped.items())

    def create_gh_issue_on_flaky_or_broken_test(self):
        if self.issue_url:
            assert False, "BUG"

        if not UserSelector.get_yes_or_no_answer(
            "Do you want to create an issue for this failure?"
        ):
            return False

        failure_reason = UserSelector.get_user_string_input(
            "Enter failure keyword from the test output identifying the problem (e.g. 'Timeout exceeded', 'Logical error', 'Result differs', etc.)",
            validator=lambda x: x in self.praktika_result.info,
        )
        title = f"Flaky test: {self.test_name}"
        body = f"""\
Failure reason: {failure_reason}
[CI report. (See job {self.job_name})]({report_url})
[cidb]({self.cidb_link})
"""
        labels = ["testing", "flaky test"]
        issue_url = GH.create_issue(
            title, body, labels, repo="ClickHouse/ClickHouse", verbose=True
        )
        if issue_url:
            print(f"Issue {issue_url} created")
            self.issue_url = issue_url
            self.praktika_result.set_clickable_label("flaky", issue_url)
        else:
            raise Exception("Failed to create issue")
        return True


class JobResultProcessor:

    @staticmethod
    def process_job_result(job_result: Result):
        print(f"Job {job_result.name} status is {job_result.status}")
        if "Stateless" in job_result.name:
            JobResultProcessor.process_stateless_job(job_result)
        elif "Integration" in job_result.name:
            JobResultProcessor.process_integration_job(job_result)
        elif "AST" in job_result.name:
            JobResultProcessor.process_ast_fuzzer_job(job_result)
        else:
            raise Exception(f"Unknown job type: {job_result.name}")

    @staticmethod
    def process_stateless_job(job_result: Result):
        print(f"Failed tests:")
        for test in job_result.results:
            print(
                test.to_stdout_formatted(
                    truncate_from_top=False, max_info_lines_cnt=20, max_line_length=200
                )
            )

    @staticmethod
    def process_integration_job(job_result: Result):
        print(f"Failed tests:")
        for test in job_result.results:
            print(
                test.to_stdout_formatted(
                    truncate_from_top=False, max_info_lines_cnt=20, max_line_length=200
                )
            )

    @staticmethod
    def process_ast_fuzzer_job(job_result: Result):
        assert False, "TODO"

    @staticmethod
    def get_pr_result(commit_status_data: CommitStatus, pr_number, commit_sha):
        if (
            commit_status_data.state
            not in (
                Result.Status.SUCCESS,
                Result.Status.FAILED,
            )
            and not FORCE_MERGE
        ):
            raise Exception(
                f"Status for {commit_status_data.context} is not completed: {commit_status_data.state} - cannot proceed"
            )
        global report_url
        report_url = f"https://s3.amazonaws.com/clickhouse-test-reports/PRs/{pr_number}/{commit_sha}/result_pr.json"
        _ = Shell.check(f"curl {report_url} -o /tmp/result_pr.json > /dev/null 2>&1")
        pr_result = Result.from_file("/tmp/result_pr.json")
        return pr_result

    @staticmethod
    def collect_all_failures(pr_result, failures):
        success_job_cnt = 0
        failed_job_cnt = 0
        skipped_job_cnt = 0
        dropped_job_cnt = 0
        running_job_cnt = 0
        pending_job_cnt = 0
        error_job_cnt = 0
        for job_result in pr_result.results:
            if job_result.is_success():
                success_job_cnt += 1
            elif job_result.is_failure():
                failed_job_cnt += 1
            elif job_result.is_skipped():
                skipped_job_cnt += 1
            elif job_result.is_dropped():
                dropped_job_cnt += 1
            elif job_result.is_running():
                running_job_cnt += 1
            elif job_result.is_pending():
                pending_job_cnt += 1
            elif job_result.is_error():
                error_job_cnt += 1
            else:
                raise Exception(f"Unknown job result status: {job_result.status}")
        assert (
            success_job_cnt
            + failed_job_cnt
            + skipped_job_cnt
            + dropped_job_cnt
            + running_job_cnt
            + pending_job_cnt
            + error_job_cnt
            == len(pr_result.results)
        )
        if pr_result.is_ok():
            print(f"All jobs are successful - ready to merge")
        else:
            print(f"Not all jobs are successful - proceed with caution")
            for job_result in pr_result.results:
                if not job_result.is_ok():
                    if job_result.results:
                        for test_result in job_result.results:
                            failures.append(
                                CIFailure(
                                    job_name=job_result.name,
                                    job_status=job_result.status,
                                    test_name=test_result.name,
                                    test_status=test_result.status,
                                    test_info=test_result.info,
                                    praktika_result=test_result,
                                )
                            )
                    else:
                        failures.append(
                            CIFailure(
                                job_name=job_result.name,
                                job_status=job_result.status,
                                test_name="",
                                test_status="",
                                test_info=job_result.info,
                                praktika_result=job_result,
                            )
                        )

    @staticmethod
    def process_sync_status(commit_status_data: CommitStatus, sha: str):
        if commit_status_data.state in (Result.Status.SUCCESS,):
            pass
        elif commit_status_data.state in (Result.Status.FAILED,):
            print(f"\nCH Sync failed for commit {commit_status_data.context}")
            if UserSelector.get_yes_or_no_answer("You sure it can be ignored?"):
                GH.post_commit_status(
                    commit_status_data.context,
                    Result.Status.SUCCESS,
                    "Ignored",
                    commit_status_data.url,
                    sha=sha,
                    repo="ClickHouse/ClickHouse",
                )
            else:
                sys.exit(0)
        elif commit_status_data.state in (Result.Status.PENDING,):
            if commit_status_data.description == "tests started":
                print(
                    f"\n{commit_status_data.context} is pending with description {commit_status_data.description}"
                )
                if UserSelector.get_yes_or_no_answer("You sure it can be ignored?"):
                    GH.post_commit_status(
                        commit_status_data.context,
                        Result.Status.SUCCESS,
                        "Ignored",
                        commit_status_data.url,
                        sha=sha,
                        repo="ClickHouse/ClickHouse",
                    )
                else:
                    sys.exit(0)
            else:
                print(
                    f"CH Sync commit status state: {commit_status_data.state} and description: {commit_status_data.description} - cannot proceed"
                )
                sys.exit(0)

    @staticmethod
    def process_mergeable_check_status(commit_status_data: CommitStatus, sha: str):
        if commit_status_data and commit_status_data.state in (Result.Status.SUCCESS,):
            pass
        elif FORCE_MERGE or commit_status_data.state in (Result.Status.FAILED,):
            if UserSelector.get_yes_or_no_answer(
                "Do you want to unblock mergeable check?"
            ):
                GH.post_commit_status(
                    CheckStatuses.MERGEABLE_CHECK,
                    Result.Status.SUCCESS,
                    "Manually overridden",
                    "",
                    sha=sha,
                    repo="ClickHouse/ClickHouse",
                )
            else:
                sys.exit(0)
        else:
            raise Exception(
                f"Mergeable check commit status state: {commit_status_data.state} and description: {commit_status_data.description} - cannot proceed"
            )


def find_existing_issues_for_failures(failures: list[CIFailure]):
    """
    Check if any of the provided failures have existing open GitHub issues.

    Args:
        failures: List of CIFailure objects to check against open GitHub issues

    Returns:
        Tuple of (failures_with_open_issue, unknown_failures) where:
        - failures_with_open_issue: failures that have existing GitHub issues
        - unknown_failures: failures without existing GitHub issues
    """
    job_failures_pairs = CIFailure.group_by_job(failures)
    failures_with_open_issue = []
    unknown_failures = []
    for job_name, job_failures in job_failures_pairs:
        print(f"\n  - {job_name}: status {len(job_failures)} failures")
        for failure in job_failures:
            if failure.test_name:
                print(f"    - {failure.test_name}: {failure.test_status}")
            else:
                print(f"    - {failure.job_name}: {failure.job_status}")
            # Check if this is a standard test name format (e.g., 12345_test_name or test_name)
            if failure.job_type == JobTypes.BUILD:
                search_in_title = failure.job_name
                labels = ["build"]
            elif failure.job_type in (JobTypes.STATELESS, JobTypes.INTEGRATION):
                if not failure.test_name:
                    print(
                        f"      --> It's looks like infrastracture problem - cannot handle it"
                    )
                    continue
                assert re.match(
                    r"^(\d{5}|test)_", failure.test_name
                ), f"Unexpected test name format: {failure.test_name}"
                search_in_title = failure.test_name
                labels = ["flaky test"]
            else:
                raise Exception(f"Unexpected job type: {failure.job_type}")

            issue = GH.find_issue(
                title=search_in_title,
                labels=labels,
                repo="ClickHouse/ClickHouse",
            )
            if issue:
                print(f"      --> Issue {issue.html_url} already exists")
                failure.issue_url = issue.html_url
                failure.praktika_result.set_clickable_label("flaky", issue.html_url)
                failure.praktika_result.set_comment("ISSUE EXISTS")
                failures_with_open_issue.append(failure)
            else:
                print(f"      --> No existing issue found for {failure.test_name}")
                unknown_failures.append(failure)

    return failures_with_open_issue, unknown_failures


def create_issues_for_failures(failures: list[CIFailure]):
    """
    Interactively create GitHub issues for failures that don't have existing issues.

    Args:
        failures: List of CIFailure objects to create issues for

    Returns:
        List of failures that still need issues (those for which issues were not created)
    """
    failures_with_created_issues = []
    job_failures_pairs = CIFailure.group_by_job(failures)
    print(f"There are failures in [{len(job_failures_pairs)}] jobs")
    for job_name, job_failures in job_failures_pairs:
        print(f"  - {job_name}: {len(job_failures)} failures")
        for failure in job_failures:
            print(f"    - {failure.test_name}: {failure.test_status}")
            # Check if this is a standard test name format (e.g., 12345_test_name or test_name)
            if re.match(r"^(\d{5}|test)_", failure.test_name):
                assert (
                    not failure.issue_url
                ), "BUG: Issue URL is already set, this should be a known issue"
                print(repr(failure))
                if failure.create_gh_issue_on_flaky_or_broken_test():
                    failures_with_created_issues.append(failure)
            else:
                # Non-standard test name format - needs special handling
                raise Exception(f"Unsupported test name format: {failure.test_name}")
    return [f for f in failures if f not in failures_with_created_issues]


if __name__ == "__main__":
    my_prs_number_and_title = Shell.get_output(
        "gh pr list --author @me --json number,title --base master --limit 20"
    )
    my_prs_number_and_title = json.loads(my_prs_number_and_title)
    pr_menu = []
    pr_menu.append((f"Enter PR number manually", 0))
    for pr_dict in my_prs_number_and_title:
        pr_number = pr_dict["number"]
        pr_title = pr_dict["title"]
        pr_menu.append((f"#{pr_number}: {pr_title}", pr_number))

    selected_pr = UserSelector.get_user_choice_from_menu(
        pr_menu, "Select a PR to merge"
    )
    if selected_pr[1] == 0:
        # PR numbers are expected to be in the range 80000-100000 for recent PRs
        pr_number = UserSelector.get_user_numeric_input(
            "Enter PR number", lambda x: x > 80000 and x < 100000
        )
    else:
        pr_number = selected_pr[1]

    pr_url = f"https://github.com/ClickHouse/ClickHouse/pull/{pr_number}"
    print(f"\nSelected PR: {selected_pr[0]}")
    print(f"PR URL: {pr_url}")

    if GH.pr_has_conflicts(pr_number, "ClickHouse/ClickHouse"):
        print("PR has conflicts, cannot merge")
        sys.exit(1)

    # Get the head commit SHA and branch name
    pr_data = Shell.get_output(f"gh pr view {pr_number} --json headRefOid,headRefName")
    pr_data = json.loads(pr_data)
    head_sha = pr_data["headRefOid"]
    print(f"Head commit SHA: {head_sha}")

    # Get commit statuses with pagination
    statuses_list = Shell.get_output(
        f"gh api repos/ClickHouse/ClickHouse/commits/{head_sha}/statuses --paginate"
    )
    statuses_list = json.loads(statuses_list)

    # Filter for specific statuses (take the first match for each context)
    required_checks = [
        CheckStatuses.PR,
        CheckStatuses.CH_INC_SYNC,
        CheckStatuses.MERGEABLE_CHECK,
    ]
    status_map = {}

    for status in statuses_list:
        context = status["context"]
        if context in required_checks and context not in status_map:
            status_map[context] = CommitStatus(
                state=status["state"],
                description=status.get("description", "N/A"),
                url=status.get("target_url", ""),
                context=context,
            )

    sync_status = status_map.get(CheckStatuses.CH_INC_SYNC)
    mergeable_check_status = status_map.get(CheckStatuses.MERGEABLE_CHECK)

    print(f"\nCommit statuses:")
    for check in required_checks:
        if check in status_map:
            state = status_map[check].state
            desc = status_map[check].description
            print(f"  - {check}: {state} - {desc}")
        else:
            print(f"  - {check}: unknown")
    print("")

    ci_failures = []
    pr_result = JobResultProcessor.get_pr_result(
        status_map[CheckStatuses.PR], pr_number, head_sha
    )
    JobResultProcessor.collect_all_failures(
        pr_result,
        failures=ci_failures,
    )

    not_finished_jobs = []
    known_failures = []
    unknown_failures = []
    unprocessed_failures = []
    for failure in ci_failures:
        if not failure.praktika_result.is_completed():
            not_finished_jobs.append(failure)
        elif failure.issue_url:
            known_failures.append(failure)
        elif failure.ignorable:
            unprocessed_failures.append(failure)
        else:
            unknown_failures.append(failure)
    pre_existing_issues_count = len(known_failures)

    if not_finished_jobs:
        if FORCE_MERGE:
            print(f"Not finished jobs:")
            for failure in not_finished_jobs:
                print(failure)
            if not UserSelector.get_yes_or_no_answer(
                "Proceed without waiting for not finished jobs?"
            ):
                sys.exit(0)
        else:
            print(
                f"There are {len(not_finished_jobs)} not finished jobs. Cannot proceed"
            )
            sys.exit(0)

    if unknown_failures:
        print("\nUnknown failures:")
        for failure in unknown_failures:
            print(failure)
        if UserSelector.get_yes_or_no_answer(
            f"There are {len(unknown_failures)} unknown failures. Check for existing GitHub issues?"
        ):
            failures_with_open_issue, unknown_failures = (
                find_existing_issues_for_failures(unknown_failures)
            )
            known_failures.extend(failures_with_open_issue)
            pre_existing_issues_count += len(failures_with_open_issue)
        else:
            sys.exit(0)

    print("\nCI failures:")
    if known_failures:
        print("\n--- Known problems ---")
        for failure in known_failures:
            print(failure)

    newly_created_issues_count = 0
    if unknown_failures:
        print("\n--- Unknown problems ---")
        for failure in unknown_failures:
            print(failure)

        if UserSelector.get_yes_or_no_answer(
            f"There are {len(unknown_failures)} unknown failures. Do you want to create an issue for any of them?"
        ):
            unknown_failures_before_creation = len(unknown_failures)
            unknown_failures = create_issues_for_failures(unknown_failures)
            newly_created_issues_count = unknown_failures_before_creation - len(
                unknown_failures
            )
            print("All failures processed")

    should_update_PR_comment = False
    if not unknown_failures:
        if unprocessed_failures:
            print("\n--- Unprocessed failures ---")
            for failure in unprocessed_failures:
                print(failure)
        question = "CI status:\n"
        if (
            unprocessed_failures
            or newly_created_issues_count > 0
            or pre_existing_issues_count > 0
        ):
            should_update_PR_comment = True
            if not_finished_jobs:
                question += f" - {len(not_finished_jobs)} not finished job{'s' if len(not_finished_jobs) != 1 else ''}\n"
            if unprocessed_failures:
                unprocessed_count = len(unprocessed_failures)
                question += f" - {unprocessed_count} unprocessed failure{'s' if unprocessed_count != 1 else ''}\n"
            if newly_created_issues_count > 0:
                question += f" - {newly_created_issues_count} issue{'s' if newly_created_issues_count != 1 else ''} just created\n"
            if pre_existing_issues_count > 0:
                question += f" - {pre_existing_issues_count} pre-existing issue{'s' if pre_existing_issues_count != 1 else ''}\n"
            question += " - all other checks passed\n"
        else:
            question = "All checks passed! Congratulations!\n"
        question += "\nDo you want to merge the PR?"
        if not UserSelector.get_yes_or_no_answer(question):
            sys.exit(0)
    else:
        print("There are unknown failures. Not merging the PR")
        sys.exit(0)

    JobResultProcessor.process_mergeable_check_status(
        mergeable_check_status, sha=head_sha
    )

    if unprocessed_failures:
        for failure in unprocessed_failures:
            failure.praktika_result.set_comment("IGNORED")

    JobResultProcessor.process_sync_status(sync_status, sha=head_sha)

    assert not unknown_failures, "BUG: unknown failures are not processed"
    if should_update_PR_comment:
        try:
            print("\nUpdating CI summary in the PR comment")
            summary_body = GH.ResultSummaryForGH.from_result(
                pr_result,
                sha=head_sha,
            ).to_markdown(pr_number, head_sha, workflow_name="PR", branch="")
            if not GH.post_updateable_comment(
                comment_tags_and_bodies={"summary": summary_body},
                pr=pr_number,
                repo="ClickHouse/ClickHouse",
                only_update=True,
                verbose=False,
            ):
                print(f"ERROR: failed to post CI summary")
        except Exception as e:
            print(f"ERROR: failed to post CI summary, ex: {e}")
            traceback.print_exc()
    if Shell.check(f"gh pr merge {pr_number} --auto"):
        print(f"PR {pr_number} auto merge has been enabled")
