### Create Virtual ENV

```
python3.10 -m venv env
```

### Install requirment.txt
```
pip install -r requirment.txt
```

### Create Database With Postgres
```
  Create database sudofire;
```

### Create Database Tables With Django - Terminal Commands
```
python manage.py makemigrations
python manage.py migrate
```

### Run Project
```
python manage.py runserver
```

# API's

### Register 
  Endpoint = /api/auth/register/ <br/>
  Method = POST <br/>
  Param = first_name, last_name, email, password <br/>

<br/>
We have User and Customer one to one mapping. The customer Mapped at user creation with <b>Django Signal</b>.
I have created a <b>signal</b> to create customer after user creations.

### Login 
  Endpoint = /api/auth/login/ <br/>
  Method = POST <br/>
  Param = email, password <br/>


## Database Backup and Upload to S3 Bucket at 2 AM Daily. Below is CRON JOB and it will run shell script daily At 2 AM 
```
0 2 * * * /bin/bash /home/arjun/Documents/projects/sudofiretest/db_backup.sh >>  /home/arjun/Documents/projects/sudofiretest/db_backup.log
```
<br>
I have created shell script to run terminal command to download database from CRON Job and written one python script to upload .sql to S3.
<br/><br/>
Please change the below credentials as you required. I have tested with actual credentials and its working fine

```
client = session.client(
    's3',
    config=botocore.config.Config(s3={'addressing_style': 'virtual'}), #  // Configures to use subdomain/virtual calling format.
    region_name='sgp11',
    endpoint_url='https://sudofire.digitaloceanspaces.com',
    aws_access_key_id='DO00U6MREJHK9IOS',
    aws_secret_access_key='QWVRFGGwe6DYOAPil/JAzhjhfs7qdsUdBDjTTSILE4qBuFcdiRBs'
)

bucket = 'sudofire_db'

```




