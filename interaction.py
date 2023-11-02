from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # Fix: options=chrome_options
driver.get('https://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys("Pavan")

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Kumar V')

email = driver.find_element(By.NAME, 'email')
email.send_keys('pkvstarscream@gmail.com')

submit_button = driver.find_element(By.CSS_SELECTOR, 'button')
submit_button.send_keys(Keys.ENTER)
# statistics_number = driver.find_element(By.CSS_SELECTOR, '#articlecount a')  # Fix: Remove 'value='
# # statistics_number.click()
#
# anyone_can_edit = driver.find_element(By.LINK_TEXT, "anyone can edit")
# # anyone_can_edit.click()
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# driver.quit()
