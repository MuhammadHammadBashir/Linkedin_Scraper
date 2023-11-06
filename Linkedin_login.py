# imports
from selenium import webdriver
import csv
from time import sleep
from parameters import file_name, linkedin_username,linkedin_password
from selenium.webdriver.common.by import By
# defining new variable passing two parameters

with open(file_name, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])
# writer = csv.writer(open(file_name, 'wb'))

# # writerow() method to the write to the file object
# writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome()

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name



username =driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[1]/div[1]/div/div/input')
# username = driver.find_element(By.CLASS_NAME, 'login-email')


# send_keys() to simulate key strokes
username.send_keys(linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name

password =driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[1]/div[2]/div/div/input')
# password = driver.find_element(By.CLASS_NAME,'login-password')

# send_keys() to simulate key strokes
password.send_keys(linkedin_password)
sleep(0.5)

# locate submit button by_xpath


sign_in_button =driver.find_element(By.XPATH,'/html/body/main/section[1]/div/div/form/div[2]/button')


# .click() to mimic button click
sign_in_button.click()