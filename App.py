from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import requests
import time

url="http://www.diva-gis.org/gdata"


donnes=requests.get(url).text

soup=BeautifulSoup(donnes, "html.parser")

liens=soup.find("select")
get_opt=liens.find_all("option")

print(get_opt[0]['value'])

##---------------------bot script-------------------------------#

for el in get_opt:
    driver = webdriver.Chrome('./chromedriver')

    driver.get(url)



    #øget_select=driver.find_element_by_name("cnt")
    #get_select.click()


    select=Select(driver.find_element(by=By.NAME, value="cnt"))

    select.select_by_value(el['value'])

    ok=driver.find_element(by=By.NAME, value="OK")
    ok.click()




    time.sleep(1)

    btn_download=driver.find_element_by_xpath("//h2[contains(text(), 'Download')]")
    btn_download.click()

    time.sleep(20)

    driver.back()



driver.quit()






