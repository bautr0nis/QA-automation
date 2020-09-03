from selenium import webdriver
import time

#Using chrome navigate directly to http://the-internet.herokuapp.com/challenging_dom
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/challenging_dom") #Opening a website

#Highlight the text in the third row of the Diceret column for two seconds.
#Creating a highlight function which we will envoke later.
def highlight(element, effect_time, color, border):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",element, s)
    original_style = element.get_attribute('style')
    apply_style("border: {0}px solid {1};".format(border, color))
    time.sleep(effect_time)
    apply_style(original_style)

open_window_elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[3]/td[6]") #Selecting an onbject
highlight(open_window_elem, 2, "blue", 5) # This will add blue 5 pixels border to element for 2 second

#Highlight the delete link in the row containing “Apeirian7” for two seconds
open_window_elem2 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[8]/td[7]/a[2]")
highlight(open_window_elem2, 2, "red", 5)

#Highlight the edit link for the row containing “Apeirian2” for two seconds.
open_window_elem3 = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr[3]/td[7]/a[1]")
highlight(open_window_elem3, 2, "green", 5)

#Highlight “Definiebas7” for two seconds, then highlight “Iuvaret7” for two seconds.
open_window_elem4 = driver.find_element_by_xpath("//td[text()='Definiebas7']")
highlight(open_window_elem4, 2, "purple", 5)

open_window_elem4 = driver.find_element_by_xpath("//td[text()='Iuvaret7']")
highlight(open_window_elem4, 2, "purple", 5)

#Click the Green button.
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/a[3]').click()