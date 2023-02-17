# This solution uses the urllib library to make a GET request to the URL and retrieve the HTML content of the webpage. The BeautifulSoup library is then used to parse the HTML content, and the find_all method is used to find all the a tags (which represent links) in the HTML. The solution then iterates over the links and prints the URL and text of each link.

# A few questions a programmer should consider when extracting links from a webpage include:

# What kind of links do you want to extract (internal, external, or both)?
# What information do you want to extract for each link (URL, text, or both)?
# Are there any specific links you want to exclude (e.g. links to social media pages or advertisements)?


import argparse
import logging
import urllib.request
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def extract_links(url):
    """Extract all the relevant links from the specified URL"""
    # Make a GET request to the URL and retrieve the HTML content
    try:
        response = urllib.request.urlopen(url)
        html_content = response.read()
    except urllib.error.URLError as e:
        logging.error(f'Failed to retrieve URL: {e}')
        return []
    except urllib.error.HTTPError as e:
        logging.error(f'HTTP error while retrieving URL: {e}')
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all the 'a' tags in the HTML
    links = soup.find_all('a')

    # Filter the links based on certain criteria
    filtered_links = [link for link in links if not (
        'facebook' in link.get('href') or
        'twitter' in link.get('href') or
        'instagram' in link.get('href') or
        'ad' in link.get('href').lower()
    )]

    return filtered_links

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract relevant links from a webpage')
    parser.add_argument('url', help='The URL of the webpage')
    parser.add_argument('--output', help='The output file to store the links')
    args = parser.parse_args()

    # Extract the relevant links from the URL
    links = extract_links(args.url)

    # Log the number of links extracted
    logging.info(f'Extracted {len(links)} relevant links')

    # Store the links in the specified output file
    if args.output:
        with open(args.output, 'w') as f:
            for link in links:
                f.write(link.get('href') + '\n')
        logging.info(f'Relevant links stored in {args.output}')

if __name__ == '__main__':
    main()
