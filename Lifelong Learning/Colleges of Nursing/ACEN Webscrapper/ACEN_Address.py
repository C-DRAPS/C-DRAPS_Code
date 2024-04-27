# TODO: This is a helper program to "ACEN Programs.py". It travels to another webpage
#  to find the address of our current accredited program (university) that
#  "ACEN Programs.py" has pulled.
import requests
from bs4 import BeautifulSoup


def getAddress(link):
    # Send an HTTP GET request to the website
    website = requests.get(link)

    # Check if the request was successful (status code 200)
    if website.status_code == 200:

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(website.content, "html.parser")

        html_p_types = soup.find_all('p')

        try:
            for item in html_p_types:
                if item.text.find("Address") != -1:
                    text = item.text
                    text_single_line = " ".join(text.split("\n")).replace("Address: ", "")
                    return text_single_line
        except:
            return None

    else:
        print("Failed to retrieve address from the website.")
        return None
