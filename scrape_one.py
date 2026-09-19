import truststore
truststore.inject_into_ssl()

import requests
from bs4 import BeautifulSoup

url = "https://oracc.museum.upenn.edu/saao/saa08/P336558/html"

# retrieving + download the page
# also checking if it was downloaded properly
response= requests.get(url)
print(response.status_code)

# turning into HTML text
# so easily parsed
soup = BeautifulSoup(response.text, "html.parser")

# finding translation spans
# finding paragraphs of class "tr"
# found in html insepction element
translations = soup.find_all("p", class_="tr")

for t in translations:
    print(t.get_text(" ", strip=True))
