from selenium import webdriver
from selenium import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time
PATH = ".\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://finance.yahoo.com/quote/%5ENSEI?p=^NSEI&.tsrc=fin-srch')
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')))
    previousPrice = 0
    exitFlag = False
    while(exitFlag == False):
        currentPrice = driver.find_element(By.XPATH,'//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]').get_attribute('value')
        if currentPrice != previousPrice:
            os.system('cls')
            print("Current Price : ",currentPrice)
            print("Press Ctrl+C to Exit...")
            previousPrice = currentPrice
        time.sleep(1)
    driver.quit()
except Exception as e:
    driver.quit()
    os.system('cls')
    print(e)