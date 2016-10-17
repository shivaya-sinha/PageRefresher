from selenium import webdriver
import time

#taking URL from user
x=raw_input("Enter the URL")

#taking the time after which page is to be refreshed
refreshrate=raw_input("Enter the number of seconds")

#changing refresh rate from string to int
refreshrate=int(refreshrate)

driver = webdriver.Firefox()
#getting proper url
driver.get("http://"+x)
while True:
	#sleep for time- refreshrate and then refresh
	time.sleep(refreshrate)
	driver.refresh()
