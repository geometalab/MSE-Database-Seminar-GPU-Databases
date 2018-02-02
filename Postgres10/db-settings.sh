#!/bin/bash
	set -o errexit
set -o pipefail
set -o nounset

function alter_system() {
	echo "Altering System parameters"
	PGUSER="$POSTGRES_USER" psql --dbname="$POSTGRES_DB" <<-EOSQL
		ALTER SYSTEM SET max_connections = '1000';
		ALTER SYSTEM SET superuser_reserved_connections = '5';
		ALTER SYSTEM SET shared_buffers = '128GB';
		ALTER SYSTEM SET effective_cache_size = '384GB';
		ALTER SYSTEM SET work_mem = '64GB';
		ALTER SYSTEM SET maintenance_work_mem = '2GB';
		ALTER SYSTEM SET min_wal_size = '4GB';
		ALTER SYSTEM SET max_wal_size = '8GB';
		ALTER SYSTEM SET checkpoint_completion_target = '0.9';
		ALTER SYSTEM SET wal_buffers = '16MB';
		ALTER SYSTEM SET default_statistics_target = '500';
		ALTER SYSTEM SET random_page_cost = '1.1';
		ALTER SYSTEM SET max_worker_processes = '40';
		ALTER SYSTEM SET max_parallel_workers = '40';
		ALTER SYSTEM SET max_parallel_workers_per_gather = '40';
		ALTER SYSTEM SET fsync = 'off';
EOSQL
}

alter_system