from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

service = Service("C:/Python/chromedriverwin64/chromedriver.exe")
driver = webdriver.Chrome(service=service)
#driver = webdriver.Chrome(service=service)
driver.get("https://adactinhotelapp.com/")

#Register
#driver.find_element(By.LINK_TEXT, "New User Register Here").click()
#time.sleep(2)
#driver.find_element(By.ID, "username").send_keys("Rajavel9594")
#driver.find_element(By.ID, "password").send_keys("Testing@123")
#driver.find_element(By.ID, "re_password").send_keys("Testing@123")
#driver.find_element(By.NAME, "full_name").send_keys("Rajavel")
#driver.find_element(By.XPATH, "//input[@name='email_add']").send_keys("rajavel9594@yopmail.com")
#driver.find_element(By.XPATH, "//input[@name='tnc_box']").click()
#recaptcha = input("Enter CAPTCHA from the screen: ")
#driver.find_element(By.ID, "captcha-form").send_keys(recaptcha)
#time.sleep(3)
#driver.find_element(By.XPATH, "//input[@name='Submit']").click()

#login
driver.find_element(By.ID, "username").send_keys("Rajavel9594")
driver.find_element(By.NAME, "password").send_keys("Testing@123")
driver.find_element(By.ID, "login").click()

time.sleep(2)
Select(driver.find_element(By.ID, "location")).select_by_visible_text("New York")
Select(driver.find_element(By.ID, "hotels")).select_by_visible_text("Hotel Sunshine")
Select(driver.find_element(By.ID, "room_type")).select_by_visible_text("Standard")
Select(driver.find_element(By.ID, "room_nos")).select_by_visible_text("1 - One")
driver.find_element(By.ID, "datepick_in").clear()
driver.find_element(By.ID, "datepick_in").send_keys("20/06/2025")
driver.find_element(By.ID, "datepick_out").clear()
driver.find_element(By.ID, "datepick_out").send_keys("25/06/2025")
Select(driver.find_element(By.ID, "adult_room")).select_by_visible_text("2 - Two")
Select(driver.find_element(By.ID, "child_room")).select_by_visible_text("0 - None")
time.sleep(2)
driver.find_element(By.ID, "Submit").click()
time.sleep(5)