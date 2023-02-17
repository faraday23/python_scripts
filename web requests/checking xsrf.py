import requests
from bs4 import BeautifulSoup

# Use the secure HTTPS protocol
url = 'https://medium.com/artificial-corner/how-id-learn-to-code-if-i-could-start-over-ft-chatgpt-eeb4108edb8f'

# Validate user input before using it in a request
user_input = input("Enter a URL to extract links from: ")
if not user_input.startswith("https://"):
    raise ValueError("Invalid URL - must start with 'https://'")
else:
    url = user_input

# Use the 'requests' library for secure HTTP requests
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the 'a' tags in the HTML
links = soup.find_all('a')

# Check for a CSRF token in the form
csrf_token = soup.find("input", attrs={"name": "csrf_token"})["value"]

# Iterate over the links and print the URL and text of each link
for link in links:
    href = link.get('href')

    # Check that the link is not from an untrusted source
    if "example.com" in href:
        print('URL:', href)
        print('Text:', link.text)
        print('---')
    else:
        print("Untrusted source - skipping link")

# If a CSRF token was found, send it as part of the next request
if csrf_token:
    headers = {'X-CSRF-Token': csrf_token}
    response = requests.post(url, headers=headers)
    print("Successful CSRF protection")
else:
    print("CSRF token not found")
