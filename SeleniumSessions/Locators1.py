import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("/Users/adithbala/Downloads/chromedriver")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://demo.nopcommerce.com/")
#driver.maximize_window() #maximize the browser window

#1. ID and NAME Locators:
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

#2. Link Text / Partial Link Text
#driver.find_element(By.LINK_TEXT,"Register").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()

# driver.get("http://automationpractice.com/index.php")

#3. classname
# sliders = driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print(len(sliders))

#tagName
# links = driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
# for i in links:
#     print(i.text)


#4. CSS Selector
driver.get("https://www.facebook.com")
driver.maximize_window()

#tag and id
#driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

#tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext")

#tag and attribute
driver.find_element(By.CSS_SELECTOR,"input[name='email']").send_keys("abc@gmail.com")

#tag, class and  attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[name='email']").send_keys("abc@gmail.com")

#5. XPath



time.sleep(5)

driver.quit()