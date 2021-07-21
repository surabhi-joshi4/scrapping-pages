from selenium import webdriver as sw
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import xlsxwriter
service = Service('D:\\Selenium Project\\chromedriver_win32\\chromedriver.exe')
service.start()
driver = sw.Remote(service.service_url)

# for holding the resultant list
element_list = []
for page in range(1,4):
	page_url="https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
	print("page Number",str(page))
	url=driver.get(page_url)
	title=driver.find_elements_by_class_name("title")
	price = driver.find_elements_by_class_name("price")
	description = driver.find_elements_by_class_name("description")
	rating = driver.find_elements_by_class_name("ratings")
	try:
		for i in range(len(title)):
			element_list.append([title[i].get_attribute('textContent'), price[i].get_attribute('textContent'), description[i].get_attribute('textContent'), rating[i].get_attribute('textContent')])
	except e:
		print(e)

	time.sleep(10)
print(element_list)

with xlsxwriter.Workbook('D:\\Selenium Project\\result.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
  
    for row_num, data in enumerate(element_list):
        worksheet.write_row(row_num, 0, data)


