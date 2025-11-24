import dataclasses


@dataclasses.dataclass
class TC:
    prefix: str
    is_sequential: bool
    comment: str


TEST_CONFIGS = [
    TC("test_atomic_drop_table/", True, "no idea why i'm sequential"),
    TC("test_attach_without_fetching/", True, "no idea why i'm sequential"),
    TC(
        "test_cleanup_dir_after_bad_zk_conn/",
        True,
        "no idea why i'm sequential",
    ),
    TC(
        "test_consistent_parts_after_clone_replica/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_crash_log/", True, "no idea why i'm sequential"),
    TC("test_cross_replication/", True, "no idea why i'm sequential"),
    TC("test_ddl_worker_non_leader/", True, "no idea why i'm sequential"),
    TC("test_delayed_replica_failover/", True, "no idea why i'm sequential"),
    TC(
        "test_dictionary_allow_read_expired_keys/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_disabled_mysql_server/", True, "no idea why i'm sequential"),
    TC("test_distributed_respect_user_timeouts/", True, "no idea why i'm sequential"),
    TC("test_dns_cache/", True, "no idea why i'm sequential"),
    TC("test_global_overcommit_tracker/", True, "no idea why i'm sequential"),
    TC("test_grpc_protocol/", True, "no idea why i'm sequential"),
    TC("test_host_regexp_multiple_ptr_records/", True, "no idea why i'm sequential"),
    TC("test_http_failover/", True, "no idea why i'm sequential"),
    TC("test_https_replication/", True, "no idea why i'm sequential"),
    TC("test_insert_into_distributed/", True, "no idea why i'm sequential"),
    TC(
        "test_insert_into_distributed_through_materialized_view/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_keeper_map/", True, "no idea why i'm sequential"),
    TC("test_keeper_multinode_simple/", True, "no idea why i'm sequential"),
    TC("test_keeper_two_nodes_cluster/", True, "no idea why i'm sequential"),
    TC("test_limited_replicated_fetches/", True, "no idea why i'm sequential"),
    TC("test_merge_tree_s3/", True, "no idea why i'm sequential"),
    TC("test_mysql_database_engine/", True, "no idea why i'm sequential"),
    TC("test_parts_delete_zookeeper/", True, "no idea why i'm sequential"),
    TC(
        "test_postgresql_replica_database_engine/",
        True,
        "no idea why i'm sequential",
    ),
    TC(
        "test_profile_max_sessions_for_user/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_quorum_inserts_parallel/", True, "no idea why i'm sequential"),
    TC("test_random_inserts/", True, "no idea why i'm sequential"),
    TC("test_replace_partition/", True, "no idea why i'm sequential"),
    TC("test_replicated_database/", True, "no idea why i'm sequential"),
    TC("test_replicated_fetches_timeouts/", True, "no idea why i'm sequential"),
    TC(
        "test_replicated_merge_tree_wait_on_shutdown/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_server_overload/", True, "no idea why i'm sequential"),
    TC("test_server_reload/", True, "no idea why i'm sequential"),
    TC("test_storage_kafka/", True, "no idea why i'm sequential"),
    TC("test_storage_kerberized_kafka/", True, "no idea why i'm sequential"),
    TC("test_storage_rabbitmq/", True, "no idea why i'm sequential"),
    TC("test_storage_s3/", True, "no idea why i'm sequential"),
    TC("test_storage_s3_queue/", True, "no idea why i'm sequential"),
    TC("test_system_flush_logs/", True, "no idea why i'm sequential"),
    TC("test_system_logs/", True, "no idea why i'm sequential"),
    TC("test_system_metrics/", True, "no idea why i'm sequential"),
    TC("test_ttl_move/", True, "no idea why i'm sequential"),
    TC("test_user_ip_restrictions/", True, "no idea why i'm sequential"),
    TC(
        "test_zookeeper_config_load_balancing/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_zookeeper_fallback_session/", True, "no idea why i'm sequential"),
    TC(
        "test_backup_restore_on_cluster/test_concurrency.py",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_database_delta/test.py", True, "no idea why i'm sequential"),
    TC("test_keeper_ipv4_fallback/test.py", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_no_spark/", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_with_spark/", True, "no idea why i'm sequential"),
    TC(
        "test_storage_iceberg_schema_evolution/",
        True,
        "no idea why i'm sequential",
    ),
    TC("test_disks_app_interactive/", True, "no idea why i'm sequential"),
    TC("test_storage_delta_disks/", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_disks/", True, "no idea why i'm sequential"),
    TC("test_storage_iceberg_concurrent/", True, "no idea why i'm sequential"),
]

IMAGES_ENV = {
    "clickhouse/dotnet-client": "DOCKER_DOTNET_CLIENT_TAG",
    "clickhouse/integration-helper": "DOCKER_HELPER_TAG",
    "clickhouse/integration-test": "DOCKER_BASE_TAG",
    "clickhouse/kerberos-kdc": "DOCKER_KERBEROS_KDC_TAG",
    "clickhouse/mysql-golang-client": "DOCKER_MYSQL_GOLANG_CLIENT_TAG",
    "clickhouse/mysql-java-client": "DOCKER_MYSQL_JAVA_CLIENT_TAG",
    "clickhouse/mysql-js-client": "DOCKER_MYSQL_JS_CLIENT_TAG",
    "clickhouse/arrowflight-server-test": "DOCKER_ARROWFLIGHT_SERVER_TAG",
    "clickhouse/mysql-php-client": "DOCKER_MYSQL_PHP_CLIENT_TAG",
    "clickhouse/nginx-dav": "DOCKER_NGINX_DAV_TAG",
    "clickhouse/postgresql-java-client": "DOCKER_POSTGRESQL_JAVA_CLIENT_TAG",
    "clickhouse/python-bottle": "DOCKER_PYTHON_BOTTLE_TAG",
    "clickhouse/integration-test-with-unity-catalog": "DOCKER_BASE_WITH_UNITY_CATALOG_TAG",
    "clickhouse/integration-test-with-hms": "DOCKER_BASE_WITH_HMS_TAG",
    "clickhouse/mysql_dotnet_client": "DOCKER_MYSQL_DOTNET_CLIENT_TAG",
}

# collected by
# SELECT
#     splitByString('::', test_name)[1] AS test_file,
#     SUM(test_duration_ms) AS dur
# FROM checks
# WHERE 1
#   AND check_name LIKE 'Integration tests%'
#   AND commit_sha = '79f4156eaa083ddd69722c267b88baa9d4091f7f'
# GROUP BY test_file
# HAVING test_file != ''
# ORDER BY dur desc
RAW_TEST_DURATIONS = """
test_storage_s3_queue/test_5.py	919861
test_storage_kafka/test_batch_fast.py	855068
test_storage_nats/test_nats_jet_stream.py	694774
test_storage_delta/test.py	672013
test_ttl_move/test.py	671458
test_storage_s3/test.py	565114
test_storage_rabbitmq/test.py	552102
test_backup_restore_on_cluster/test_concurrency.py	415740
test_executable_table_function/test.py	364769
test_replicated_database/test.py	343224
test_lost_part_during_startup/test.py	332874
test_distributed_respect_user_timeouts/test.py	319880
test_restore_db_replica/test.py	315577
test_storage_kafka/test_batch_slow_1.py	310037
test_keeper_two_nodes_cluster/test.py	304696
test_s3_aws_sdk_has_slightly_unreliable_behaviour/test.py	300260
test_storage_iceberg_with_spark/test_cluster_table_function.py	284176
test_multiple_disks/test.py	280238
test_max_bytes_ratio_before_external_order_group_by_for_server/test.py	267506
test_database_delta/test.py	262773
test_refreshable_mat_view_replicated/test.py	259151
test_kafka_bad_messages/test.py	249033
test_storage_kafka/test_batch_slow_2.py	244217
test_database_replicated_settings/test.py	243100
test_checking_s3_blobs_paranoid/test.py	235503
test_backup_restore_s3/test.py	234928
test_storage_s3_queue/test_1.py	231253
test_storage_azure_blob_storage/test.py	224839
test_refreshable_mv/test.py	211114
test_http_handlers_config/test.py	210504
test_throttling/test.py	209559
test_merge_tree_s3/test.py	204936
test_backup_restore_new/test.py	200887
test_storage_s3_queue/test_2.py	200201
test_storage_nats/test_nats_core.py	189272
test_storage_kafka/test_batch_slow_5.py	186282
test_storage_kafka/test_compression_codec.py	179084
test_storage_kafka/test_batch_slow_4.py	174778
test_concurrent_ttl_merges/test.py	174271
test_named_collections/test.py	171955
test_drop_is_lock_free/test.py	171746
test_dns_cache/test.py	171235
test_mysql57_database_engine/test.py	163370
test_refreshable_mat_view/test.py	159628
test_refreshable_mv_skip_old_temp_table_ddls/test.py	151861
test_async_load_databases/test.py	151666
test_ytsaurus/test_tables.py	151173
test_storage_s3_queue/test_0.py	151113
test_storage_kafka/test_batch_slow_6.py	150220
test_crash_log/test.py	148926
test_backup_restore_new/test_cancel_backup.py	143395
test_hedged_requests/test.py	141425
test_http_failover/test.py	140832
test_storage_kerberized_kafka/test.py	140575
test_statistics_cache/test.py	140410
test_storage_iceberg_schema_evolution/test_evolved_schema_simple.py	139259
test_distributed_ddl/test.py	137954
test_backward_compatibility/test_aggregate_function_state.py	137004
test_postgresql_database_engine/test.py	131360
test_system_logs/test_system_logs.py	129082
test_system_clusters_actual_information/test.py	119871
test_keeper_zookeeper_converter/test.py	119248
test_config_decryption/test_wrong_settings.py	118960
test_replicated_mutations/test.py	118856
test_dictionaries_all_layouts_separate_sources/test_mongo.py	115842
test_dictionaries_dependency/test.py	114353
test_library_bridge/test.py	114180
test_lost_part/test.py	113143
test_backward_compatibility/test_functions.py	111970
test_storage_iceberg_concurrent/test_concurrent_reads.py	108694
test_backup_restore_on_cluster/test_cancel_backup.py	108165
test_mask_sensitive_info/test.py	103399
test_postpone_failed_tasks/test.py	102515
test_plain_rewritable_backward_compatibility/test.py	100660
test_storage_s3_queue/test_3.py	98498
test_backward_compatibility/test_convert_ordinary.py	95946
test_rename_column/test.py	95863
test_storage_iceberg_with_spark/test_position_deletes.py	94721
test_system_merges/test.py	93855
test_storage_iceberg_schema_evolution/test_array_evolved_nested.py	91999
test_scheduler/test.py	91777
test_ttl_replicated/test.py	90526
test_keeper_internal_secure/test.py	84714
test_distributed_load_balancing/test.py	84027
test_backup_restore_on_cluster/test.py	83986
test_odbc_interaction/test.py	83790
test_keeper_map/test.py	82380
test_storage_kafka/test_batch_slow_0.py	81073
test_restore_replica/test.py	79112
test_replicated_fetches_bandwidth/test.py	78419
test_cleanup_dir_after_bad_zk_conn/test.py	78170
test_ytsaurus/test_dictionaries.py	77605
test_mysql_protocol/test.py	77338
test_dictionaries_redis/test.py	76269
test_storage_s3_queue/test_4.py	76105
test_postgresql_replica_database_engine/test_1.py	75934
test_parallel_replicas_insert_select/test.py	74100
test_dictionaries_all_layouts_separate_sources/test_clickhouse_local.py	72810
test_dictionaries_all_layouts_separate_sources/test_mysql.py	72753
test_dictionaries_all_layouts_separate_sources/test_http.py	72482
test_dictionaries_all_layouts_separate_sources/test_clickhouse_remote.py	72411
test_dictionaries_all_layouts_separate_sources/test_https.py	72340
test_modify_engine_on_restart/test_ordinary.py	72209
test_keeper_incorrect_config/test.py	69946
test_keeper_password/test.py	67861
test_keeper_three_nodes_two_alive/test.py	67838
test_recompression_ttl/test.py	67807
test_store_cleanup/test.py	66985
test_version_update_after_mutation/test.py	66892
test_dictionaries_update_and_reload/test.py	66321
test_s3_plain_rewritable_rotate_tables/test.py	65710
test_log_query_probability/test.py	65647
test_storage_hudi/test.py	65636
test_postgresql_replica_database_engine/test_3.py	64557
test_s3_table_function_with_http_proxy/test.py	63448
test_ddl_worker_replicas/test.py	63288
test_s3_table_function_with_https_proxy/test.py	62983
test_scheduler_cpu_preemptive/test.py	62778
test_random_inserts/test.py	62746
test_postgresql_replica_database_engine/test_2.py	62325
test_memory_limit_observer/test.py	61658
test_keeper_force_recovery/test.py	61068
test_distributed_ddl_parallel/test.py	60943
test_mutations_hardlinks/test.py	60660
test_cluster_discovery/test_auxiliary_keeper.py	60615
test_mysql_database_engine/test.py	59438
test_alter_moving_garbage/test.py	58351
test_rocksdb_options/test.py	58097
test_storage_iceberg_with_spark/test_minmax_pruning.py	57725
test_keeper_disks/test.py	57244
test_storage_alias_replicated/test.py	57238
test_keeper_nodes_remove/test.py	56944
test_keeper_back_to_back/test.py	56627
test_inserts_with_keeper_retries/test.py	56616
test_storage_iceberg_with_spark/test_metadata_file_selection.py	56380
test_storage_iceberg_with_spark/test_metadata_file_format_with_uuid.py	56240
test_drop_database_replica/test.py	54898
test_cluster_discovery/test_dynamic_clusters.py	54554
test_transposed_metric_log/test.py	54498
test_globs_in_filepath/test.py	52901
test_filesystem_cache/test.py	52091
test_disk_over_web_server/test.py	51986
test_s3_plain_rewritable/test.py	50176
test_executable_dictionary/test.py	48847
test_s3_table_functions/test.py	47959
test_database_backup/test.py	47937
test_keeper_mntr_pressure/test.py	47278
test_replicated_user_defined_functions/test.py	47130
test_broken_projections/test.py	47104
test_keeper_invalid_digest/test.py	46294
test_keeper_auth/test.py	46283
test_parallel_replicas_invisible_parts/test.py	46119
test_hedged_requests_parallel/test.py	45733
test_quorum_inserts/test.py	44971
test_cluster_discovery/test.py	44490
test_role/test.py	44371
test_memory_limit/test.py	43774
test_postgresql_replica_database_engine/test_0.py	43390
test_backup_restore_new/test_shutdown_wait_backup.py	42317
test_replicated_database_cluster_groups/test.py	41730
test_reloading_storage_configuration/test.py	41387
test_parallel_replicas_over_distributed/test.py	40546
test_storage_iceberg_with_spark/test_system_iceberg_metadata.py	40322
test_keeper_force_recovery_single_node/test.py	39371
test_jbod_ha/test.py	39347
test_keeper_nodes_add/test.py	39071
test_system_metrics/test.py	38822
test_storage_rabbitmq/test_failed_connection.py	38521
test_system_logs_recreate/test.py	37773
test_merge_tree_azure_blob_storage/test.py	37469
test_dictionaries_all_layouts_separate_sources/test_file.py	36792
test_distributed_directory_monitor_split_batch_on_failure/test.py	36405
test_storage_iceberg_with_spark/test_writes_mutate_delete.py	36302
test_limited_replicated_fetches/test.py	35919
test_keeper_snapshot_small_distance/test.py	35891
test_dictionaries_ddl/test.py	35789
test_named_collections_if_exists_on_cluster/test.py	35292
test_disk_configuration/test.py	35271
test_storage_mongodb/test.py	35212
test_backup_restore_keeper_map/test.py	35119
test_userspace_page_cache/test.py	34728
test_disk_access_storage/test.py	33992
test_old_parts_finally_removed/test.py	33870
test_s3_cluster_restart/test.py	33412
test_keeper_block_acl/test.py	33349
test_dictionaries_dependency_xml/test.py	33291
test_async_metrics_in_cgroup/test.py	32930
test_check_table/test.py	32924
test_keeper_nodes_move/test.py	32669
test_scheduler_query/test.py	32650
test_replicated_users/test.py	32045
test_storage_iceberg_schema_evolution/test_tuple_evolved_nested.py	31615
test_acme_tls/test_multi_node.py	31552
test_https_s3_table_function_with_http_proxy_no_tunneling/test.py	31270
test_storage_iceberg_with_spark/test_partition_pruning.py	31270
test_host_regexp_multiple_ptr_records/test.py	30731
test_replicated_table_attach/test.py	30658
test_dictionaries_postgresql/test.py	30558
test_parallel_replicas_all_marks_read/test.py	30327
test_server_overload/test.py	30083
test_row_policy/test.py	30036
test_executable_user_defined_function/test.py	29885
test_replicated_database_recover_digest_mismatch/test.py	29613
test_storage_iceberg_with_spark/test_explicit_metadata_file.py	29378
test_insert_distributed_async_send/test.py	29334
test_merge_tree_s3_failover/test.py	29268
test_MemoryTracking/test.py	28976
test_naive_bayes_bad_models/test.py	28802
test_concurrent_queries_restriction_by_query_kind/test.py	28479
test_named_collections_encrypted/test.py	28407
test_azure_blob_storage_plain_rewritable/test.py	28257
test_storage_iceberg_with_spark/test_schema_evolution_with_time_travel.py	28138
test_merge_tree_load_parts/test.py	27971
test_storage_postgresql/test.py	27662
test_ddl_on_cluster_stop_waiting_for_offline_hosts/test.py	27485
test_keeper_broken_logs/test.py	27173
test_storage_kafka_sasl/test.py	27081
test_zookeeper_config/test_password.py	26588
test_polymorphic_parts/test.py	26546
test_encrypted_disk/test.py	26503
test_keeper_feature_flags_config/test.py	26174
test_keeper_s3_snapshot/test.py	26156
test_tmp_policy/test.py	25933
test_keeper_max_append_byte_size/test.py	25463
test_backup_restore_on_cluster/test_disallow_concurrency.py	25430
test_keeper_znode_time/test.py	25417
test_user_directories/test.py	25126
test_catboost_evaluate/test.py	25089
test_consistent_parts_after_clone_replica/test.py	25047
test_keeper_snapshots/test.py	24955
test_storage_kafka/test_produce_http_interface.py	24728
test_on_cluster_timeouts/test.py	24582
test_storage_iceberg_no_spark/test_writes_statistics_by_minmax_pruning.py	24393
test_atomic_drop_table/test.py	24297
test_modify_engine_on_restart/test.py	24284
test_storage_iceberg_with_spark/test_writes_create_partitioned_table.py	24201
test_keeper_reconfig_replace_leader_in_one_command/test.py	24155
test_storage_iceberg_with_spark/test_writes_mutate_update.py	23990
test_jbod_balancer/test.py	23951
test_dictionaries_all_layouts_separate_sources/test_mongo_uri.py	23886
test_dictionaries_all_layouts_separate_sources/test_executable_hashed.py	23686
test_system_detached_tables/test.py	23135
test_keeper_three_nodes_start/test.py	23053
test_group_array_element_size/test.py	22991
test_storage_iceberg_schema_evolution/test_evolved_schema_complex.py	22670
test_keeper_multinode_simple/test.py	22250
test_jemalloc_global_profiler/test.py	22076
test_undrop_query/test.py	21998
test_storage_mysql/test.py	21794
test_keeper_snapshot_on_exit/test.py	21589
test_move_ttl_broken_compatibility/test.py	21566
test_file_schema_inference_cache/test.py	21527
test_merges_memory_limit/test.py	21316
test_async_insert_memory/test.py	21282
test_s3_storage_conf_proxy/test.py	21182
test_storage_iceberg_schema_evolution/test_array_evolved_with_struct.py	21180
test_storage_iceberg_with_spark/test_metadata_file_selection_from_version_hint.py	20837
test_restore_external_engines/test.py	20769
test_system_flush_logs/test.py	20736
test_parallel_replicas_custom_key_failover/test.py	20711
test_executable_user_defined_functions_config_reload/test.py	20473
test_dictionaries_config_reload/test.py	20418
test_delayed_replica_failover/test.py	20322
test_user_valid_until/test.py	20099
test_database_disk_setting/test.py	19924
test_dictionaries_all_layouts_separate_sources/test_executable_cache.py	19837
test_keeper_reconfig_remove_many/test.py	19763
test_keeper_reconfig_replace_leader/test.py	19597
test_allow_feature_tier/test.py	19570
test_replicated_access/test.py	19421
test_storage_iceberg_with_spark/test_schema_inference.py	19090
test_attach_partition_using_copy/test.py	19067
test_storage_iceberg_no_spark/test_writes_multiple_files.py	19042
test_backward_compatibility/test_vertical_merges_from_compact_parts.py	19004
test_ttl_multilevel_group_by/test.py	18824
test_warning_broken_tables/test.py	18795
test_replicated_merge_tree_with_auxiliary_zookeepers/test.py	18786
test_log_lz4_streaming/test.py	18676
test_parallel_replicas_custom_key_load_balancing/test.py	18496
test_zookeeper_config_load_balancing/test.py	18378
test_dictionaries_wait_for_load/test.py	18357
test_shutdown_wait_unfinished_queries/test.py	18355
test_storage_kafka/test_intent_sizes.py	18154
test_replicated_merge_tree_wait_on_shutdown/test.py	18094
test_scheduler_cpu/test.py	18049
test_library_bridge/test_exiled.py	17969
test_grant_and_revoke/test_with_table_engine_grant.py	17849
test_s3_cluster/test.py	17826
test_storage_iceberg_with_spark/test_delete_files.py	17762
test_storage_delta/test_cdf.py	17682
test_database_glue/test.py	17429
test_user_defined_object_persistence/test.py	17217
test_storage_iceberg_with_spark/test_writes.py	17120
test_secure_socket/test.py	17009
test_keeper_mntr_data_size/test.py	16976
test_remove_stale_moving_parts/test.py	16685
test_parts_delete_zookeeper/test.py	16564
test_kafka_bad_messages/test_1.py	16501
test_attach_without_fetching/test.py	16228
test_dictionaries_mysql/test.py	16012
test_zookeeper_connection_log/test.py	15922
test_insert_into_distributed/test.py	15921
test_database_iceberg/test.py	15879
test_storage_s3/test_invalid_env_credentials.py	15731
test_startup_scripts_execution_state/test.py	15590
test_storage_iceberg_with_spark/test_iceberg_snapshot_reads.py	15243
test_https_replication/test.py	15053
test_storage_iceberg_disks/test.py	14882
test_suggestions/test.py	14863
test_storage_delta_disks/test.py	14764
test_manipulate_statistics/test.py	14732
test_keeper_reconfig_remove/test.py	14665
test_backup_restore/test.py	14618
test_mutations_with_merge_tree/test.py	14525
test_reload_zookeeper/test.py	14521
test_config_decryption/test_wrong_settings_zk.py	14400
test_lightweight_updates/test.py	14276
test_acme_tls/test_single_node.py	13759
test_storage_s3_queue/test_parallel_inserts.py	13709
test_restart_server/test.py	13433
test_partition/test.py	13419
test_enable_user_name_access_type/test.py	13393
test_https_replication/test_change_ip.py	13320
test_search_orphaned_parts/test.py	13315
test_keeper_four_word_command/test.py	13211
test_join_set_family_s3/test.py	13103
test_replace_partition/test.py	13067
test_quorum_inserts_parallel/test.py	13032
test_startup_scripts/test.py	12941
test_replicated_fetches_timeouts/test.py	12877
test_format_schema_source/test.py	12690
test_quota/test.py	12632
test_dictionaries_replace/test.py	12627
test_cancel_freeze/test.py	12426
test_storage_kafka/test_schema_registry_skip_bytes.py	12397
test_move_partition_to_volume_async/test.py	12265
test_keeper_remove_acl/test.py	12196
test_storage_iceberg_schema_evolution/test_map_evolved_nested.py	12157
test_multi_access_storage_role_management/test.py	12061
test_distributed_ddl/test_replicated_alter.py	12043
test_zookeeper_config/test_secure.py	11933
test_config_yaml_full/test.py	11901
test_read_only_table/test.py	11819
test_keeper_reconfig_add/test.py	11784
test_parallel_replicas_custom_key/test.py	11774
test_recovery_replica/test.py	11584
test_keeper_session/test.py	11488
test_interserver_dns_retires/test.py	11481
test_grpc_protocol/test.py	11251
test_sql_roles_for_xml_users/test.py	11117
test_lazy_database/test.py	11074
test_reload_auxiliary_zookeepers/test.py	11035
test_keeper_persistent_log/test.py	11001
test_disk_checker/test.py	10998
test_storage_iceberg_with_spark/test_minmax_pruning_with_null.py	10997
test_replicated_merge_tree_compatibility/test.py	10788
test_config_reloader_interval/test.py	10681
test_config_xml_full/test.py	10615
test_distributed_inter_server_secret/test.py	10588
test_s3_storage_conf_new_proxy/test.py	10546
test_modify_engine_on_restart/test_zk_path_exists.py	10517
test_rocksdb_read_only/test.py	10497
test_keeper_persistent_log_multinode/test.py	10461
test_transactions/test.py	10412
test_recovery_time_metric/test.py	10371
test_config_xml_yaml_mix/test.py	10357
test_config_yaml_main/test.py	10343
test_replication_credentials/test.py	10266
test_compressed_marks_restart/test.py	10218
test_table_db_num_limit/test.py	10191
test_replication_without_zookeeper/test.py	10177
test_system_ddl_worker_queue/test.py	10124
test_distributed_default_database/test.py	10121
test_server_start_and_ip_conversions/test.py	10103
test_storage_iceberg_with_spark/test_writes_create_table.py	9990
test_config_xml_main/test.py	9956
test_default_compression_codec/test.py	9937
test_storage_iceberg_with_spark/test_writes_schema_evolution.py	9927
test_force_restore_data_flag_for_keeper_dataloss/test.py	9903
test_modify_engine_on_restart/test_storage_policies.py	9894
test_system_start_stop_listen/test.py	9880
test_trace_log_build_id/test.py	9824
test_storage_delta/test_imds.py	9708
test_keeper_snapshots_multinode/test.py	9480
test_hot_reload_storage_policy/test.py	9400
test_trace_collector_serverwide/test.py	9288
test_keeper_memory_soft_limit/test.py	9257
test_storage_policies/test.py	9248
test_filesystem_cache_uninitialized/test.py	9202
test_server_reload/test.py	9125
test_config_yaml_merge_keys/test.py	9091
test_validate_threadpool_writer_pool_size/test.py	9071
test_backup_restore_on_cluster_with_checksum_data_file_name/test.py	9069
test_settings_profile/test.py	8921
test_select_access_rights/test_main.py	8803
test_drop_replica_with_auxiliary_zookeepers/test.py	8794
test_dictionaries_redis/test_long.py	8745
test_storage_iceberg_with_spark/test_writes_with_partitioned_table.py	8734
test_storage_iceberg_with_spark/test_explanation.py	8683
test_system_reload_async_metrics/test_async_metrics_invalid_settings.py	8588
test_allowed_url_from_config/test.py	8478
test_insert_into_distributed_sync_async/test.py	8444
test_keeper_profiler/test.py	8395
test_keeper_map_retries/test.py	8352
test_ddl_worker_non_leader/test.py	8251
test_config_substitutions/test.py	8239
test_mark_cache_profile_events/test.py	8034
test_always_fetch_merged/test.py	7966
test_s3_access_headers/test.py	7958
test_match_process_uid_against_data_owner/test.py	7867
test_remote_blobs_naming/test_backward_compatibility.py	7771
test_replica_is_active/test.py	7538
test_sharding_key_from_default_column/test.py	7522
test_replicated_merge_tree_encryption_codec/test.py	7453
test_storage_iceberg_with_spark/test_optimize.py	7440
test_database_iceberg_nessie_catalog/test.py	7440
test_stop_insert_when_disk_close_to_full/test.py	7340
test_asynchronous_metrics_pk_bytes_fields/test.py	7338
test_backup_restore_azure_blob_storage/test.py	7324
test_consistant_parts_after_move_partition/test.py	7249
test_keeper_restore_from_snapshot/test.py	7207
test_max_suspicious_broken_parts/test.py	7184
test_storage_iceberg_with_spark/test_restart_broken_s3.py	7136
test_format_cannot_allocate_thread/test.py	7115
test_zookeeper_fallback_session/test.py	7035
test_keeper_restore_from_snapshot/test_disk_s3.py	7026
test_insert_distributed_load_balancing/test.py	7018
test_storage_iceberg_with_spark/test_bucket_partition_pruning.py	6999
test_async_insert_adaptive_busy_timeout/test.py	6952
test_dictionary_asynchronous_metrics/test.py	6913
test_prometheus_protocols/test_write_read.py	6853
test_extreme_deduplication/test.py	6838
test_parallel_replicas_distributed_skip_shards/test.py	6752
test_storage_numbers/test.py	6647
test_merge_tree_s3_with_cache/test.py	6570
test_backup_log/test.py	6425
test_temporary_data/test.py	6393
test_fix_metadata_version/test.py	6359
test_aliases_in_default_expr_not_break_table_structure/test.py	6279
test_storage_iceberg_schema_evolution/test_correct_column_mapper_is_chosen.py	6216
test_storage_iceberg_with_spark/test_multiple_iceberg_file.py	6195
test_storage_iceberg_with_spark/test_partition_by.py	6182
test_distributed_format/test.py	6172
test_force_drop_table/test.py	6126
test_filesystem_layout/test.py	6089
test_system_queries/test.py	6043
test_session_settings_table/test.py	5921
test_threadpool_readers/test.py	5846
test_concurrent_threads_soft_limit/test.py	5834
test_non_default_compression/test.py	5793
test_storage_iceberg_with_spark/test_writes_from_zero.py	5754
test_access_for_functions/test.py	5733
test_insert_distributed_async_extra_dirs/test.py	5662
test_dictionary_allow_read_expired_keys/test_default_reading.py	5632
test_graphite_merge_tree_typed/test.py	5627
test_modify_engine_on_restart/test_args.py	5626
test_dictionary_allow_read_expired_keys/test_dict_get_or_default.py	5618
test_dictionary_allow_read_expired_keys/test_dict_get.py	5614
test_table_function_mongodb/test.py	5580
test_modify_engine_on_restart/test_unusual_path.py	5565
test_permissions_drop_replica/test.py	5520
test_backup_restore_on_cluster/test_huge_concurrent_restore.py	5460
test_version_update/test.py	5276
test_reload_max_table_size_to_drop/test.py	5264
test_read_temporary_tables_on_failure/test.py	5238
test_backward_compatibility/test_ip_types_binary_compatibility.py	5226
test_grpc_protocol_ssl/test.py	5224
test_mutation_fetch_fallback/test.py	5210
test_cleanup_after_start/test.py	5206
test_placement_info/test.py	5190
test_profile_max_sessions_for_user/test.py	5179
test_dictionary_allow_read_expired_keys/test_default_string.py	5178
test_keeper_watches/test.py	5155
test_modify_engine_on_restart/test_mv.py	5147
test_send_request_to_leader_replica/test.py	5069
test_log_family_s3/test.py	5066
test_system_logs_comment/test.py	5023
test_max_suspicious_broken_parts_replicated/test.py	4999
test_plain_rewr_legacy_layout/test.py	4991
test_replicated_merge_tree_encrypted_disk/test.py	4987
test_graphite_merge_tree/test.py	4980
test_mutations_in_partitions_of_merge_tree/test.py	4957
test_disks_app_func/test.py	4919
test_restart_with_unavailable_azure/test.py	4885
test_limit_materialized_view_count/test.py	4855
test_disabled_access_control_improvements/test_row_policy.py	4780
test_attach_with_different_projections_or_indices/test.py	4751
test_storage_redis/test.py	4725
test_temporary_data_in_cache/test.py	4720
test_detached_parts_metrics/test.py	4695
test_server_startup_and_shutdown_logs/test.py	4584
test_backup_restore_storage_policy/test.py	4556
test_shutdown_static_destructor_failure/test.py	4544
test_alter_database_on_cluster/test.py	4532
test_create_user_and_login/test.py	4482
test_settings_constraints/test.py	4452
test_reloading_settings_from_users_xml/test.py	4415
test_storage_iceberg_with_spark/test_writes_complex_type.py	4378
test_build_sets_from_multiple_threads/test.py	4338
test_no_merges_volume_ttl/test.py	4321
test_backward_compatibility/test_rocksdb_upgrade.py	4312
test_insert_into_distributed_through_materialized_view/test.py	4287
test_storage_iceberg_with_spark/test_types.py	4283
test_attach_partition_with_large_destination/test.py	4170
test_merge_tree_check_part_with_cache/test.py	4125
test_access_control_on_cluster/test.py	4124
test_reload_clusters_config/test.py	4103
test_replicated_merge_tree_s3/test.py	4068
test_storage_iceberg_with_spark/test_read_in_order.py	4059
test_cross_replication/test.py	3918
test_jemalloc_percpu_arena/test.py	3906
test_drop_replica/test.py	3871
test_alter_on_mixed_type_cluster/test.py	3821
test_reload_client_certificate/test.py	3798
test_part_log_table/test.py	3767
test_async_connect_to_multiple_ips/test.py	3747
test_storage_kafka/test_zookeeper_locks.py	3739
test_trace_log_memory_context/test.py	3717
test_storage_iceberg_with_spark/test_metadata_cache.py	3663
test_parallel_replicas_failover/test.py	3639
test_ldap_external_user_directory/test.py	3624
test_fetch_memory_usage/test.py	3595
test_covered_by_broken_exists/test.py	3581
test_distributed_insert_backward_compatibility/test.py	3552
test_overcommit_tracker/test.py	3533
test_dictionary_ddl_on_cluster/test.py	3489
test_storage_azure_blob_storage/test_cluster.py	3470
test_azure_blob_storage_native_copy/test.py	3426
test_replicated_merge_tree_thread_schedule_timeouts/test.py	3416
test_cgroup_limit/test.py	3395
test_distributed_ddl_on_cross_replication/test.py	3391
test_arrowflight_interface/test.py	3382
test_backward_compatibility/test_block_marshalling.py	3370
test_storage_s3/test_sts.py	3358
test_tcp_handler_connection_limits/test.py	3334
test_asynchronous_metric_log_table/test.py	3322
test_distributed_async_insert_for_node_changes/test.py	3312
test_arrowflight_interface/test_ticket_expiration.py	3297
test_backup_restore_on_cluster/test_slow_rmt.py	3293
test_sync_replica_on_cluster/test.py	3272
test_keeper_dynamic_log_level/test.py	3245
test_backup_restore_on_cluster/test_two_shards_two_replicas.py	3217
test_prometheus_protocols/test_different_table_engines.py	3202
test_session_log/test.py	3183
test_os_thread_nice_value/test.py	3177
test_dictionaries_select_all/test.py	3151
test_backup_restore_s3/test_throttling.py	3128
test_jbod_load_balancing/test.py	3116
test_storage_iceberg_with_spark/test_partition_pruning_with_subquery_set.py	3088
test_runtime_configurable_cache_size/test.py	3069
test_force_deduplication/test.py	3040
test_insert_over_http_query_log/test.py	3039
test_settings_constraints_distributed/test.py	3034
test_distributed_ddl_password/test.py	3022
test_check_table_name_length_2/test.py	2997
test_ddl_alter_query/test.py	2996
test_storage_iceberg_with_spark/test_single_iceberg_file.py	2978
test_input_format_parallel_parsing_memory_tracking/test.py	2956
test_system_logs_hostname/test_replicated.py	2844
test_zookeeper_config/test.py	2842
test_select_access_rights/test_from_system_tables.py	2830
test_storage_iceberg_with_spark/test_writes_multiple_threads.py	2698
test_global_overcommit_tracker/test.py	2649
test_storage_iceberg_with_spark/test_writes_create_version_hint.py	2635
test_attach_table_normalizer/test.py	2609
test_prometheus_protocols/test_evaluation.py	2604
test_storage_iceberg_no_spark/test_writes_multiple_threads.py	2587
test_parallel_replicas_snapshot_from_initiator/test.py	2522
test_arrowflight_storage/test.py	2522
test_git_import/test.py	2520
test_compression_nested_columns/test.py	2504
test_http_connection_drain_before_reuse/test.py	2465
test_send_crash_reports/test.py	2383
test_system_reconnect_zookeeper/test.py	2375
test_settings_from_server/test.py	2361
test_dremio_engine/test.py	2349
test_database_iceberg_lakekeeper_catalog/test.py	2344
test_ssl_cert_authentication/test.py	2339
test_wrong_db_or_table_name/test.py	2323
test_parallel_replicas_protocol/test.py	2287
test_ddl_worker_with_loopback_hosts/test.py	2265
test_postgresql_protocol/test.py	2257
test_dotnet_client/test.py	2241
test_storage_iceberg_with_spark/test_writes_drop_table.py	2225
test_parallel_replicas_no_replicas/test.py	2203
test_ddl_worker_retry_when_dropping_db_failed/test.py	2194
test_broken_part_during_merge/test.py	2169
test_cow_policy/test.py	2165
test_analyzer_compatibility/test.py	2151
test_database_hms/test.py	2146
test_disabled_access_control_improvements/test_select_from_system_tables.py	2139
test_validate_only_initial_alter_query/test_replicated_database.py	2132
test_storage_url/test.py	2120
test_compatibility_merge_tree_settings/test.py	2107
test_external_http_authenticator/test.py	2087
test_file_cluster/test.py	2074
test_profile_events_s3/test.py	2068
test_mutations_with_projection/test.py	2066
test_s3_cluster_insert_select/test.py	2064
test_dictionaries_access/test.py	2004
test_encrypted_disk_replication/test.py	1996
test_ddl_config_hostname/test.py	1965
test_drop_if_empty/test.py	1924
test_default_role/test.py	1923
test_disable_insertion_and_mutation/test.py	1893
test_external_cluster/test.py	1893
test_s3_low_cardinality_right_border/test.py	1878
test_reload_certificate/test.py	1836
test_storage_iceberg_with_spark/test_writes_field_partitioning.py	1797
test_replicated_s3_zero_copy_drop_partition/test.py	1796
test_materialized_view_restart_server/test.py	1756
test_storage_iceberg_with_spark/test_relevant_iceberg_schema_chosen.py	1744
test_format_schema_on_server/test.py	1737
test_storage_iceberg_with_spark/test_minmax_pruning_for_arrays_and_maps_subfields_disabled.py	1737
test_keeper_four_word_command/test_allow_list.py	1640
test_executable_udf_names_in_system_query_log/test.py	1637
test_keeper_http_control/test.py	1623
test_move_partition_to_disk_on_cluster/test.py	1591
test_part_uuid/test.py	1575
test_storage_iceberg_with_spark/test_filesystem_cache.py	1547
test_storage_iceberg_schema_evolution/test_full_drop.py	1528
test_create_query_constraints/test.py	1525
test_default_compression_in_mergetree_settings/test.py	1516
test_backward_compatibility/test_parallel_replicas_protocol.py	1470
test_fetch_partition_should_reset_mutation/test.py	1448
test_concurrent_queries_for_all_users_restriction/test.py	1434
test_storage_iceberg_with_spark/test_compressed_metadata.py	1416
test_alternative_keeper_config/test.py	1384
test_matview_union_replicated/test.py	1360
test_table_functions_access_rights/test.py	1342
test_storage_iceberg_no_spark/test_read_in_order_with_pyiceberg.py	1337
test_distributed_over_distributed/test.py	1333
test_attach_backup_from_s3_plain/test.py	1329
test_optimize_on_insert/test.py	1252
test_concurrent_queries_for_user_restriction/test.py	1232
test_backward_compatibility/test_memory_bound_aggregation.py	1229
test_max_authentication_methods_per_user/test.py	1220
test_distributed_storage_configuration/test.py	1148
test_log_levels_update/test.py	1145
test_merge_tree_load_marks/test.py	1141
test_keeper_max_request_size/test.py	1131
test_truncate_database/test_replicated.py	1122
test_alter_settings_on_cluster/test.py	1115
test_allowed_client_hosts/test.py	1110
test_shard_names/test.py	1106
test_backward_compatibility/test_aggregation_with_out_of_order_buckets.py	1104
test_replicated_database_interserver_host/test.py	1092
test_drop_no_local_path/test.py	1082
test_timezone_config/test.py	1081
test_composable_protocols/test.py	1079
test_replicated_database_alter_modify_order_by/test.py	1079
test_deduplicated_attached_part_rename/test.py	1076
test_backup_restore_on_cluster/test_different_versions.py	1071
test_codec_encrypted/test.py	1070
test_merge_tree_prewarm_cache/test.py	1057
test_prefer_global_in_and_join/test.py	1055
test_merge_table_over_distributed/test.py	1043
test_storage_url_http_headers/test.py	1040
test_parallel_replicas_increase_error_count/test.py	1033
test_table_function_redis/test.py	1025
test_structured_logging_json/test.py	1022
test_default_database_on_cluster/test.py	1017
test_fetch_partition_from_auxiliary_zookeeper/test.py	1006
test_alter_comment_on_cluster/test.py	998
test_s3_style_link/test.py	996
test_format_avro_confluent/test.py	984
test_intersecting_parts/test.py	982
test_storage_iceberg_with_spark/test_writes_different_path_format_error.py	980
test_password_constraints/test.py	968
test_backward_compatibility/test_const_node_optimization.py	959
test_disk_name_virtual_column/test.py	941
test_s3_with_https/test.py	934
test_cluster_discovery/test_password.py	927
test_memory_profiler_min_max_borders/test.py	926
test_sql_user_defined_functions_on_cluster/test.py	921
test_storage_iceberg_no_spark/test_time_travel_bug_fix_validation.py	915
test_peak_memory_usage/test.py	912
test_replicated_merge_tree_replicated_db_ttl/test.py	891
test_attach_table_from_s3_plain_readonly/test.py	891
test_text_log_level/test.py	889
test_truncate_database/test_distributed.py	883
test_grant_and_revoke/test_without_table_engine_grant.py	880
test_cluster_all_replicas/test.py	861
test_s3_imds/test_simple.py	845
test_replicated_detach_table/test.py	841
test_attach_without_checksums/test.py	838
test_s3_imds/test_session_token.py	814
test_prometheus_endpoint/test.py	806
test_merge_tree_empty_parts/test.py	797
test_check_table_name_length/test.py	776
test_user_zero_database_access/test_user_zero_database_access.py	770
test_failed_async_inserts/test.py	769
test_groupBitmapAnd_on_distributed/test.py	756
test_ssh/test.py	753
test_ssh_keys_authentication/test.py	738
test_freeze_table/test.py	733
test_fetch_partition_with_outdated_parts/test.py	733
test_backward_compatibility/test_normalized_count_comparison.py	719
test_storage_iceberg_with_spark/test_pruning_nullable_bug.py	709
test_old_versions/test.py	704
test_authentication/test.py	700
test_tlsv1_3/test.py	700
test_dictionary_custom_settings/test.py	699
test_storage_iceberg_no_spark/test_writes_nullable_bugs2.py	692
test_user_ip_restrictions/test.py	691
test_distributed_config/test.py	689
test_aggregation_memory_efficient/test.py	668
test_storage_dict/test.py	666
test_backward_compatibility/test_short_strings_aggregation.py	652
test_dot_in_user_name/test.py	648
test_sql_user_impersonate/test.py	639
test_groupBitmapAnd_on_distributed/test_groupBitmapAndState_on_distributed_table.py	618
test_geoparquet/test.py	598
test_kerberos_auth/test.py	592
test_replicated_engine_arguments/test.py	588
test_config_hide_in_preprocessed/test.py	578
test_storage_azure_blob_storage/test_check_after_upload.py	575
test_reload_query_masking_rules/test.py	567
test_backward_compatibility/test_select_aggregate_alias_column.py	567
test_replicated_database/test_settings_recover_lost_replica.py	552
test_custom_settings/test.py	530
test_database_disk/test.py	529
test_enabling_access_management/test.py	523
test_storage_iceberg_no_spark/test_writes_with_compression_metadata.py	518
test_server_keep_alive/test.py	510
test_unknown_column_dist_table_with_alias/test.py	510
test_disabled_mysql_server/test.py	508
test_distributed_system_query/test.py	506
test_system_reload_async_metrics/test.py	502
test_backward_compatibility/test_aggregate_fixed_key.py	488
test_merge_tree_settings_constraints/test.py	488
test_accept_invalid_certificate/test.py	485
test_parallel_replicas_skip_shards/test.py	462
test_zero_copy_expand_macros/test.py	460
test_storage_s3_intelligent_tier/test.py	439
test_parquet_page_index/test.py	437
test_keeper_path_acl/test.py	436
test_user_grants_from_config/test.py	426
test_server_initialization/test.py	421
test_buffer_profile/test.py	408
test_backup_s3_storage_class/test.py	401
test_explain_estimates/test.py	373
test_alter_update_cast_keep_nullable/test.py	362
test_replicated_parse_zk_metadata/test.py	354
test_dictionaries_null_value/test.py	324
test_inherit_multiple_profiles/test.py	324
test_scram_sha256_password_with_replicated_zookeeper_replicator/test.py	309
test_config_decryption/test.py	308
test_storage_iceberg_with_spark/test_cluster_table_function_with_partition_pruning.py	295
test_internal_queries_not_counted/test.py	294
test_disks_app_interactive/test.py	283
test_range_hashed_dictionary_types/test.py	282
test_replicated_merge_tree_config/test.py	259
test_custom_dashboards/test.py	259
test_backward_compatibility/test_insert_profile_events.py	258
test_dictionaries_with_invalid_structure/test.py	257
test_disk_types/test.py	257
test_max_rows_to_read_leaf_with_view/test.py	249
test_settings_randomization/test.py	244
test_endpoint_macro_substitution/test.py	244
test_s3_storage_class/test.py	244
test_render_log_file_name_templates/test.py	238
test_relative_filepath/test.py	227
test_backward_compatibility/test.py	196
test_block_structure_mismatch/test.py	193
test_storage_url_with_proxy/test.py	185
test_storage_iceberg_no_spark/test_graceful_error_not_configured_iceberg_metadata_log.py	180
test_storage_iceberg_no_spark/test_writes_create_table_bugs.py	180
test_unambiguous_alter_commands/test.py	180
test_profile_settings_and_constraints_order/test.py	179
test_passing_max_partitions_to_read_remotely/test.py	179
test_backward_compatibility/test_cte_distributed.py	179
test_shard_level_const_function/test.py	167
test_backward_compatibility/test_old_client_with_replicated_columns.py	164
test_disks_app_other_disk_types/test.py	150
test_http_and_readonly/test.py	138
test_async_logger_metrics/test.py	134
test_remote_function_view/test.py	129
test_replica_can_become_leader/test.py	129
test_replicating_constants/test.py	115
test_delayed_remote_source/test.py	115
test_keeper_compression/test_with_compression.py	115
test_keeper_compression/test_without_compression.py	115
test_ssh/test_options_propagation_enabled.py	110
test_host_regexp_hosts_file_resolution/test.py	101
test_keeper_availability_zone/test.py	92
test_keeper_ipv4_fallback/test.py	81
test_tcp_handler_http_responses/test_case.py	71
test_remote_prewhere/test.py	67
test_union_header/test.py	65
test_config_decryption/test_zk.py	65
test_config_decryption/test_zk_secure.py	65
test_keeper_and_access_storage/test.py	65
test_keeper_secure_client/test.py	65
test_logs_level/test.py	64
test_keeper_client/test.py	44
test_http_native/test.py	33
test_tcp_handler_interserver_listen_host/test_case.py	6
test_config_corresponding_root/test.py	0
test_userspace_page_cache/test_incorrect_limits.py	0
test_concurrent_backups_s3/test.py	0
"""


def _parse_raw_durations(raw: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for line in raw.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # Accept both tab- and space-separated formats; last token is duration
        parts = line.split()
        try:
            duration = int(parts[-1])
        except Exception:
            continue
        path = " ".join(parts[:-1])
        out[path] = duration
    return out


TEST_DURATIONS: dict[str, int] = _parse_raw_durations(RAW_TEST_DURATIONS)


def get_optimal_test_batch(
    tests: list[str], total_batches: int, batch_num: int, num_workers: int
) -> tuple[list[str], list[str]]:
    """
    @tests - all tests to run
    @total_batches - total number of batches
    @batch_num - current batch number
    @num_workers - number of parallel workers in a batch
    returns optimal subset of parallel tests for batch_num and optimal subset of sequential tests for batch_num, based on data in TEST_DURATIONS.
    Test files not present in TEST_DURATIONS will be distributed by round robin.
    The function optimizes tail latency of batch with num_workers parallel workers.
    The function works in a deterministic way, so that batch calculated on the other machine with the same input generates the same result.
    """
    # parallel_skip_prefixes sanity check
    for test_config in TEST_CONFIGS:
        assert any(
            test_file.removeprefix("./").startswith(test_config.prefix)
            for test_file in tests
        ), f"No test files found for prefix [{test_config.prefix}] in [{tests}]"

    sequential_test_modules = [
        test_file
        for test_file in tests
        if any(test_file.startswith(test_config.prefix) for test_config in TEST_CONFIGS)
    ]
    parallel_test_modules = [
        test_file for test_file in tests if test_file not in sequential_test_modules
    ]

    if batch_num > total_batches:
        raise ValueError(f"batch_num must be in [1, {total_batches}], got {batch_num}")

    # Helper: group tests by their top-level directory (prefix)
    #  same prefix tests are grouped together to minimize docker pulls in test fixtures in each job batch
    def group_by_prefix(items: list[str]) -> dict[str, list[str]]:
        groups: dict[str, list[str]] = {}
        for it in sorted(items):
            prefix = it.split("/", 1)[0]
            groups.setdefault(prefix, []).append(it)
        return groups

    # Parallel groups and Sequential groups separated to allow distinct packing
    parallel_groups = group_by_prefix(parallel_test_modules)
    sequential_groups = group_by_prefix(sequential_test_modules)

    # Compute group durations as sum of known test durations within the group
    def groups_with_durations(groups: dict[str, list[str]]):
        known_groups: list[tuple[str, int]] = []  # (prefix, duration)
        unknown_groups: list[str] = []  # prefixes with zero known duration
        for prefix, items in sorted(groups.items()):
            dur = sum(TEST_DURATIONS.get(t, 0) for t in items)
            if dur > 0:
                known_groups.append((prefix, dur))
            else:
                unknown_groups.append(prefix)
        # Sort known by (-duration, prefix) for deterministic LPT
        known_groups.sort(key=lambda x: (-x[1], x[0]))
        # Sort unknown prefixes to make RR deterministic
        unknown_groups.sort()
        return known_groups, unknown_groups

    p_known, p_unknown = groups_with_durations(parallel_groups)
    s_known, s_unknown = groups_with_durations(sequential_groups)

    # Prepare batch containers and weights
    parallel_batches: list[list[str]] = [[] for _ in range(total_batches)]
    parallel_weights: list[int] = [0] * total_batches

    # LPT assign known-duration parallel groups
    for prefix, dur in p_known:
        idx = min(range(total_batches), key=lambda i: (parallel_weights[i], i))
        # prefix, dur sorted in p_known starting with longest duration - keep the order in batches to decrease tail latency
        parallel_batches[idx].extend(parallel_groups[prefix])
        parallel_weights[idx] += dur

    # Sort tests within each batch by duration (longest first) to minimize tail latency
    # when tests are picked by workers from the queue
    for idx in range(total_batches):
        parallel_batches[idx].sort(key=lambda x: (-TEST_DURATIONS[x], x))

    # Round-robin assign unknown-duration parallel groups
    for i, prefix in enumerate(p_unknown):
        idx = i % total_batches
        parallel_batches[idx].extend(parallel_groups[prefix])

    # Sequential batches: start from scaled parallel weights to account for worker concurrency
    sequential_batches: list[list[str]] = [[] for _ in range(total_batches)]
    sequential_weights: list[int] = [0] * total_batches

    # LPT assign known-duration sequential groups
    for prefix, dur in s_known:
        idx = min(range(total_batches), key=lambda i: (sequential_weights[i], i))
        # prefix, dur sorted in s_known starting with longest duration - keep the order in batches to decrease tail latency
        sequential_batches[idx].extend(sequential_groups[prefix])
        sequential_weights[idx] += dur

    # Round-robin assign unknown-duration sequential groups
    for i, prefix in enumerate(s_unknown):
        idx = i % total_batches
        sequential_batches[idx].extend(sequential_groups[prefix])

    print(
        f"Batches parallel weights: [{[weight // num_workers // 1000 for weight in parallel_weights]}]"
    )
    print(f"Batches weights: [{[weight // 1000 for weight in sequential_weights]}]")

    # Sanity check (non-fatal): ensure total test count preserved
    total_assigned = sum(len(b) for b in parallel_batches) + sum(
        len(b) for b in sequential_batches
    )
    assert total_assigned == len(tests)

    return parallel_batches[batch_num - 1], sequential_batches[batch_num - 1]
