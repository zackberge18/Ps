from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
PATH=r"C:\Users\zackb\PycharmProjects\ps\p4\chromedriver.exe"


driver=webdriver.Chrome(PATH)
driver.get("https://clickspeedtest.com/")
button=driver.find_element_by_id("clicker")
for _ in range(2):
    time.sleep(1)
    for i in range(50):
        button.click()
    time.sleep(6)
    close_button=driver.find_element_by_xpath('//*[@id="speedModal"]/div/div/div[1]/button')
    close_button.click()
    time.sleep(2)
    reset=driver.find_element_by_xpath('//*[@id="reset"]')

    time.sleep(1)
    reset.click()
    time.sleep(10)

driver.quit()