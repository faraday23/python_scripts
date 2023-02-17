# This script first defines the MySQL database credentials and the Azure Storage credentials. It then creates a backup directory and a backup file with a timestamp in the filename.

# The script uses the mysqldump command to create a backup of the MySQL database and save it to the backup file. It then uses the Azure Storage Python SDK to connect to the Azure Storage account, create the container if it doesn't exist, and upload the backup file to the container.

# Finally, the script loops through the backups in the container and deletes any backups that are older than 7 days.

# To use this script, you will need to replace the placeholder values for the MySQL and Azure Storage credentials with your actual credentials, and set the BACKUP_DIR variable to the path of the backup directory on your system. You will also need to install the Azure Storage Python SDK by running pip install azure-storage-blob in your command prompt or terminal.

# This script can be run on a regular basis using a tool like cron (on Linux) or Task Scheduler (on Windows) to ensure that regular backups are created and stored in the Azure Storage account.

import os
import time
import subprocess
from datetime import datetime
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# MySQL database credentials
MYSQL_USER = 'user'
MYSQL_PASSWORD = 'password'
MYSQL_HOST = 'localhost'
MYSQL_DATABASE = 'mydb'

# Azure Storage credentials
STORAGE_CONNECTION_STRING = 'your_connection_string'
CONTAINER_NAME = 'backups'

# Backup directory
BACKUP_DIR = '/path/to/backup/directory'

# Backup file name
backup_name = 'mydb_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.sql'

# Create the backup directory if it doesn't exist
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# Create the backup file
backup_path = os.path.join(BACKUP_DIR, backup_name)
cmd = f"mysqldump -u {MYSQL_USER} -p{MYSQL_PASSWORD} -h {MYSQL_HOST} {MYSQL_DATABASE} > {backup_path}"
subprocess.call(cmd, shell=True)

# Connect to the Azure Storage account
blob_service_client = BlobServiceClient.from_connection_string(STORAGE_CONNECTION_STRING)

# Create the container if it doesn't exist
container_client = blob_service_client.get_container_client(CONTAINER_NAME)
if not container_client.exists():
    container_client.create_container()

# Upload the backup file to Azure Storage
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=backup_name)
with open(backup_path, 'rb') as data:
    blob_client.upload_blob(data)

# Delete backups older than 7 days
for blob in container_client.list_blobs():
    if (datetime.now() - blob.last_modified).days > 7:
        blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob.name)
        blob_client.delete_blob()
