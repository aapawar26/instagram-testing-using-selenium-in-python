from selenium import webdriver
import time


user = input("Enter email/phone/username : ")
pas = input("Enter password : ")

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')


user_send = driver.find_element_by_xpath("//input[@name='username']")
user_send.send_keys(user)


pas_send = driver.find_element_by_xpath("//input[@name='password']")
pas_send.send_keys(pas)


login_button = driver.find_element_by_class_name('L3NKy')
login_button.click()

time.sleep(5)
driver.close()
