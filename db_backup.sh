#! /bin/bash
source /home/arjun/Documents/projects/python_envs/sudofire_env/bin/activate
export PYTHONPATH=/home/arjun/Documents/projects/python_envs/sudofire_env/bin/
cd /home/arjun/Documents/projects/sudofiretest/db_backup/

# Download Database
PGPASSWORD="test" pg_dump -U test1 --clean test1 > test1.sql

# Upload to S3
python /home/arjun/Documents/projects/sudofiretest/db_backup/db_upload.py