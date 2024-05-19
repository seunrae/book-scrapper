from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
PATH = "python-scraper/chromedriver"

service = Service(executable_path=PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://books.toscrape.com/")

links_set = set()
count = 0
ordered_list = driver.find_element(By.CSS_SELECTOR, "ol")



while len(links_set) < 20:
	book_list = ordered_list.find_elements(By.CSS_SELECTOR, "li")
	
	for list in book_list:
		link = list.find_element(By.CSS_SELECTOR, "a")
		href = link.get_attribute("href")
		links_set.add(href)
	
	next_list = driver.find_element(By.CLASS_NAME, "pager")
	next_button = next_list.find_element(By.CSS_SELECTOR, ".next > a")

	if count == 5:
		break
	
	next_button.click()
	count = count + 1
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li")))


for link in links_set:
	driver.get(link)

	book_name = driver.find_element(By.CSS_SELECTOR, "h1").text
	book_price = driver.find_element(By.CLASS_NAME, "price_color").text
	availability = driver.find_element(By.CSS_SELECTOR, ".instock.availability").text
	description = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/article/p").text


	print("Name: ", book_name)
	print("Price: ", book_price)
	print("Availability: ", availability)
	print("Description: ", description)
	print()






driver.quit()

