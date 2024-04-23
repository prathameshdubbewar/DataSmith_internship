import urllib.request
from urllib.error import HTTPError

def fetch_webpage(url):
    try:
        response = urllib.request.urlopen(url)
        print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error: Failed to fetch the webpage - {e}")

url = input("Enter the URL of the webpage: ")

fetch_webpage(url)
