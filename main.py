from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By 

time.sleep(5)
driver.get("https://practicetestautomation.com/practice-test-login/")

username_locator = driver.find_element(By.ID, "username")
username_locator.send_keys("student")

password_locator = driver.find_element(By.NAME, "password")

password_locator.send_keys("Password123")
time.sleep(7)

submit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
submit_button_locator.click()
time.sleep(7)

actual_url=driver.current_url
assert actual_url=="https://practicetestautomation.com/logged-in-successfully/"

text_locator = driver.find_element(By.TAG_NAME, "h1")
actual_text=text_locator.text
assert actual_text=="Logged In Successfully"

log_out_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator.is_displayed()
