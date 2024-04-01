import requests

def read_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print("Webpage content is:")
        print(response.text)  
    except requests.RequestException as e:
        print("Error:", e)

url = input("Enter the URL of the webpage: ")

read_webpage(url)
