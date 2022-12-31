import requests, re, time
from bs4 import BeautifulSoup



#search engines urls 
search_engines_urls =  [
                        'https://search.yahoo.com/search?p=',\
                      'https://google.com/search?q=',\
                       'https://www.bing.com/search?q=',\
                        'https://www.baidu.com/s?wd=']

# Dictionary to hold email formats for each bank
#regex for email matching

regexEmail = re.compile(r'.{1,65}@([^\/()]{1,65}?)\.(com|org|bank|gov|net)')
#finding domain of bank given bank name
def find_bank_domain(bank_name, counter = 0):
           
      if counter <len(search_engines_urls):
          try:
              bank_name = "+".join(bank_name.upper().split())
              # Search Google for the bank's website
              if "BANK" not in bank_name:
                  bank_name += '+BANK'
              search_query = f"{bank_name}+email+format"
              search_url = search_engines_urls[counter] + search_query
              search_response = requests.get(search_url)
              if search_response.status_code == 429:
                  #search_engines_urls.pop(counter)  
                  return find_bank_domain(bank_name, counter+1)
              if search_response.status_code == 500:
                  time.sleep(1000)
                  return find_bank_domain(bank_name, counter)    
              search_query2 = f"{bank_name}+email"
              search_url_2 = search_engines_urls[counter] + search_query
              search_response_2= requests.get(search_url_2)
              
                  
              search_soup = BeautifulSoup(search_response.text, "html.parser")
              search_soup_2 = BeautifulSoup(search_response_2.text, "html.parser")
              # Extract the first search result (assumed to be the bank's website)
              #first_result = search_soup.find("div", {"class": "yuRUbf"})
              first_result = search_soup.find_all("body")
              second_result = search_soup.find_all("body")
              #print(first_result[0].get_text())
              results = regexEmail.search(first_result[0].get_text()+second_result[0].get_text())
              
              return (results.group(1)+'.'+results.group(2),search_engines_urls[counter])
               
          except:
              if counter == len(search_engines_urls):  
                    print(search_response.status_code, search_response_2.status_code)  
                    return (None,search_engines_urls[counter])
              else:
                    return find_bank_domain(bank_name, counter+1)
      else:
            
          return (-1,'None')

     
