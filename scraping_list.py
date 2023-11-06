# import requests
# from bs4 import BeautifulSoup
# import re
# import urllib.parse
# from urllib.parse import urlparse
# import time
# def googleSearch(query):
#     g_clean = [ ] #this is the list we store the search results
#     url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query)#this is the actual query we are going to scrape
#     try:
#             html = requests.get(url)
#             if html.status_code==200:
#                 soup = BeautifulSoup(html.text, 'lxml')
#                 a = soup.find_all('a') # a is a list
#                 for i in a:
#                     k = i.get('href')
#                     try:
#                         m = re.search("(?P<url>https?://[^\s]+)", k)
#                         n = m.group(0)
#                         rul = n.split('&')[0]
#                         domain = urlparse(rul)
#                         if(re.search('google.com', domain.netloc)):
#                             continue
#                         else:
#                             g_clean.append(rul)
#                     except:
#                         continue
#     except Exception as ex:
#             print(str(ex))
#     finally:
#         return g_clean
    
# query = 'site:linkedin.com/in/ AND "python developer" AND "London"'
# link_list = googleSearch(query)

# print(link_list)



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import time
from selenium.webdriver.common.by import By
import csv
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
driver = webdriver.Chrome()
# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search bar element and type your query
search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')

print(search_box)
search_query = 'site:linkedin.com/in/ AND "real estate" AND "australia"'
search_box.send_keys(search_query)

# Press 'Enter' to perform the search
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load
time.sleep(3)  # You can adjust the wait time based on your internet speed

seen_urls = set()

with open('australia_search_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'URL'])

    num_scrolls = 100  # Total number of times to scroll and check for more results button
    for i in range(num_scrolls):
        print("num_scrolls :", i)
        search_results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc")
        for result in search_results:
            link = result.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            if link not in seen_urls:
                seen_urls.add(link)
                title = result.find_element(By.CSS_SELECTOR, ".DKV0Md").text
                writer.writerow([title, link])

        try:
            # Try clicking the "More results" button if it appears
            more_results_button = driver.find_element(By.CLASS_NAME, 'RVQdVd')
            more_results_button.click()
            print(f"Clicked 'More results'")
            time.sleep(5)
        except (NoSuchElementException, ElementClickInterceptedException):
            # If the button is not found or not clickable, scroll instead
            print(f"Scrolling {i + 1}/{num_scrolls}")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Wait for the page to load more results

driver.quit()