from datetime import datetime
from urllib.parse import urlparse, urljoin

import boto3
import botocore

from botocore.exceptions import ClientError

session = boto3.session.Session()
client = session.client(
    's3',
    config=botocore.config.Config(s3={'addressing_style': 'virtual'}), #  // Configures to use subdomain/virtual calling format.
    region_name='sgp11',
    endpoint_url='https://sudofire.digitaloceanspaces.com',
    aws_access_key_id='DO00U6MREJHK9IOS',
    aws_secret_access_key='QWVRFGGwe6DYOAPil/JAzhjhfs7qdsUdBDjTTSILE4qBuFcdiRBs'
)

bucket = 'sudofire_db'

db_file_path = "test1.sql"
upload_with_file_name = "test1_"+str(datetime.today().date())+".sql"

try:
    client.upload_file(db_file_path, bucket, upload_with_file_name)
    s3_url = client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': upload_with_file_name
        },
        ExpiresIn=3000
    )
    s3_url = urljoin(s3_url, urlparse(s3_url).path)
    
    # We have to implement logger or trigger email instead of print message
    if s3_url:        
        print("file uploaded successfully. The file url is ", s3_url)
    else:
        print("some issues with file upload")
except ClientError as e:
    print("Client Error === ", e)


