import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv

# Init chrome with options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-incognito")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# Load site into browser
driver = webdriver.Chrome(chrome_options=chrome_options)
url = 'https://facebook.com/saved/?cref=28'
driver.get(url)
# Username and password for facebook
USERNAME = ""
PASSWORD = ""
driver.find_element_by_id('email').send_keys(USERNAME)
driver.find_element_by_id('pass').send_keys(PASSWORD)
driver.find_element_by_id('loginbutton').click()

last_height = driver.execute_script("return document.body.scrollHeight")

new_height = -1

# Gives browser time to load new content
SCROLL_PAUSE_TIME = 2

# Stop once we scolled through all content
while last_height != new_height:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")

    last_height = new_height


articles = driver.find_elements(By.XPATH, '//*[@target="_blank"]')

articleList = []
for article in articles:
    #print(i.text)
    tempArticle = [article.get_attribute('href'), article.text]
    l.append(tmp)

# Remove duplicates from list
articleList = set(articleList)

# Save articles to file
csvfile = 'savedArticles.csv'
with open(csvfile, "w") as output:
	writer = csv.writer(output, lineterminator='\n')
	for article in articleList:
		writer.writerow(article) 
