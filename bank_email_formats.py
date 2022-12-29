import requests, re
from bs4 import BeautifulSoup

# List of bank names
 

# Dictionary to hold email formats for each bank
email_formats = {}
regexEmail = re.compile(r'.{1,65}@(.{1,65}?)\.(com|org|bank|gov)')
# Iterate through the list of bank names
#for bank_name in bank_names:
def find_bank_extension(bank_name):    
      try:
          bank_name = "+".join(bank_name.upper().split())
          # Search Google for the bank's website
          if "BANK" not in bank_name:
              bank_name += '+BANK'
          search_query = f"{bank_name}+email"
          search_url = f"https://google.com/search?q={search_query}"
          search_response = requests.get(search_url)
          search_query2 = f"{bank_name}+email+format"
          search_url_2 = f"https://google.com/search?q={search_query}"
          search_response_2= requests.get(search_url_2)
          if search_response.status_code == 429 or search_response_2.status_code==429:
              exit()
          search_soup = BeautifulSoup(search_response.text, "html.parser")
          search_soup_2 = BeautifulSoup(search_response_2.text, "html.parser")
          # Extract the first search result (assumed to be the bank's website)
          #first_result = search_soup.find("div", {"class": "yuRUbf"})
          first_result = search_soup.find_all("body")
          second_result = search_soup.find_all("body")
          #print(first_result[0].get_text())
          results = regexEmail.search(first_result[0].get_text()+second_result[0].get_text())
          return results.groups()[0]
           
      except:
          return None

 
