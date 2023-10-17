from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=C:\Github\python-whatsapp-messages\whatsapp-web\data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://web.whatsapp.com')

time.sleep(20)

driver.find_element(By.XPATH, "//*[@title='Eu']").click()

time.sleep(5)

message_field = driver.find_element(By.XPATH, "//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
message_field.send_keys("Message to be sent!")

time.sleep(5)

message_field.send_keys(Keys.ENTER)

time.sleep(5)