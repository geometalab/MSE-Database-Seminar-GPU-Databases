#!/bin/bash
	set -o errexit
set -o pipefail
set -o nounset

function alter_system() {
	echo "Altering System parameters"
	PGUSER="$POSTGRES_USER" psql --dbname="$POSTGRES_DB" <<-EOSQL
		alter system set autovacuum_work_mem = '4GB';
		alter system set checkpoint_completion_target = '0.9';
		alter system set checkpoint_timeout = '20min';
		alter system set datestyle = 'iso, mdy';
		alter system set default_statistics_target = '500';
		alter system set default_text_search_config = 'pg_catalog.english';
		alter system set dynamic_shared_memory_type = 'posix';
		alter system set effective_cache_size = '96GB';
		alter system set fsync = 'off';
		alter system set lc_messages = 'en_US.utf8';
		alter system set lc_monetary = 'en_US.utf8';
		alter system set lc_numeric = 'en_US.utf8';
		alter system set lc_time = 'en_US.utf8';
		alter system set listen_addresses = '*';
		alter system set log_checkpoints = 'on';
		alter system set log_temp_files = '1MB';
		alter system set log_timezone = 'UTC';
		alter system set maintenance_work_mem = '96GB';
		alter system set max_connections = '20';
		alter system set random_page_cost = '1.1';
		alter system set shared_buffers = '96GB';
		alter system set synchronous_commit = 'off';
		alter system set temp_buffers = '120MB';
		alter system set timezone = 'UTC';
		alter system set track_counts = 'on';
		alter system set wal_buffers = '16MB';
		alter system set max_wal_size = '5GB';
		alter system set work_mem = '6GB';
EOSQL
}

alter_system