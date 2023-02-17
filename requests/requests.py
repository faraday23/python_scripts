# For this challenge, you will build a python script that makes both a GET request and a POST request. The GET request should make a call to a 3rd-party API, such as the Twitter API, and store the result in a variable. The POST request should also make a call to a 3rd-party API, such as the Twitter API, and store the result in a variable. 

# Once both requests have been made, your python script should print the result of both requests. Make sure to include error-handling to catch any potential errors that may occur. 

# Good luck!


import requests

# set the authorization header
headers = {'Authorization': 'Bearer <your_access_token>'}

# make a GET request to the Twitter API
try:
    response = requests.get('https://api.twitter.com/1.1/statuses/home_timeline.json', headers=headers)
    response.raise_for_status() # raise exception if the request fails
    get_result = response.json()
except requests.exceptions.RequestException as e:
    print("Error making GET request:", e)
    get_result = None

# make a POST request to the Twitter API
try:
    payload = {'status': 'This is a test tweet from the Twitter API'}
    response = requests.post('https://api.twitter.com/1.1/statuses/update.json', headers=headers, data=payload)
    response.raise_for_status() # raise exception if the request fails
    post_result = response.json()
except requests.exceptions.RequestException as e:
    print("Error making POST request:", e)
    post_result = None

# print the result of both requests
print("Result of GET request:", get_result)
print("Result of POST request:", post_result)
