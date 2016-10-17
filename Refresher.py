from selenium import webdriver
x=raw_input("Enter the URL")
refreshrate=raw_input("Enter the number of seconds")
refreshrate=int(refreshrate)
driver = webdriver.Firefox()
driver.get("http://"+x)
while True:
	driver.refresh()
