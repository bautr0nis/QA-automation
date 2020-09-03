# Import webdriver for automation
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #need to send keystrokes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # Faced issue with not be able to click element, so used this function to wait for it to be clickable.
from selenium.webdriver.support import expected_conditions as EC
import time #For user to see something

driver = webdriver.Chrome()
driver.get("https://www.tiketa.lt/EN/search") #Opening a website

#Writing a Forum to a textbook
text_area = driver.find_element_by_name('sf_TextFilter')
text_area.send_keys("Forum")
driver.find_element_by_xpath("//body").click() #Simulating a click

#Select Kaunas from a drop down list
driver.find_element_by_id("dropdownMenu3").click() #Expanding drop down menu
driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]/div/div[1]/div/form/div[2]/div[1]/div[2]/div/div/div/div/ul/li[3]/a").click()

#Choosing start & end dates
timefield_start = driver.find_element_by_name('sf_DateFrom')
timefield_start.click()
timefield_start.send_keys("2020-09-01")

timefield_end = driver.find_element_by_name('sf_DateTo')
timefield_end.click()
timefield_end.send_keys("2021-12-31")

#Selecting search button

Search_button = driver.find_element_by_xpath("/html/body/div[10]/div/div/div/div[2]/div/div[1]/div/form/div[4]/button")
Search_button.send_keys(Keys.RETURN)

#Buying a ticket to “Intelligent Forum”
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div/div[2]/div/div[2]/div[3]/div/div/div/a/div[1]/img'))).click()
driver.find_element_by_xpath("/html/body/div[11]/div/div/div/div[2]/div/div[1]/div/div[3]/div[2]/div/div[4]/div/div/a").click()


# Buying without registration
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"btnNoLogin"))).click()
time.sleep(20)

#NOTE:Faced issue with CAPTCHA, so I selected objects myself... Couldn't find quick solution for this, so hopefully you won't judge me

#Selecting a 40$ ticket and searching for them
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[11]/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div[3]/div[1]/label"))).click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,"btnFindTickets"))).click()

#NOTE2 : In the end I basically coudln't bypass CAPTCHA Image test as they were giving me more and more to verify. (Not 100% sure if the last line is correct as I couldn't check the last time if everything works)

time.sleep(5)

#Closing a test
driver.quit()