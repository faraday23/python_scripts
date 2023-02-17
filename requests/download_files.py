# This script uses the requests library to download a file from a website and save it to a local file. The requests.head method is used to send a HEAD request to the URL to get the file size, and the content-length header is used to calculate the progress of the download.

# The script uses the stream=True parameter in the requests.get method to download the file in chunks and save it to the local file using the open function. The progress of the download is printed to the console using the print function and the end and flush parameters.

# The script also includes a function to calculate the MD5 hash of a file, which is used to verify that the downloaded file is not corrupt. The expected MD5 hash is hard-coded in the expected_md5 variable and the actual MD5 hash is calculated using the md5 function. If the actual MD5 hash does not match the expected MD5 hash, the downloaded file is deleted and an exception is raised. Otherwise, the path to the downloaded file is printed to the console.

# To use this script, you will need to replace the url and file_path variables with the URL of the file to download and the local path to save the file, respectively. You will also need to modify the expected_md5 variable to match the MD5 hash of the file you are downloading.


import os
import requests
import hashlib

# URL of the file to download
url = 'https://example.com/file.zip'

# Local path to save the file
file_path = '/path/to/local/file.zip'

# Buffer size for downloading the file (in bytes)
buffer_size = 1024

# Function to calculate the MD5 hash of a file
def md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# Send a HEAD request to the URL to get the file size
response = requests.head(url)
if response.status_code != 200:
    raise Exception(f"Failed to download file: HTTP status code {response.status_code}")
file_size = int(response.headers.get('content-length', 0))

# Create the parent directory if it doesn't exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Download the file in chunks and save to the local file
progress = 0
with requests.get(url, stream=True) as response:
    response.raise_for_status()
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=buffer_size):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                progress += len(chunk)
                print(f"\rDownloading {progress}/{file_size} bytes ({int(progress/file_size*100)}%)", end='', flush=True)

# Verify the downloaded file using its MD5 hash
expected_md5 = '1234567890abcdef'
actual_md5 = md5(file_path)
if actual_md5 != expected_md5:
    os.remove(file_path)
    raise Exception(f"Downloaded file is corrupt: expected MD5 hash {expected_md5}, actual MD5 hash {actual_md5}")
else:
    print(f"\nDownloaded file saved to {file_path}")