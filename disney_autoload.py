from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
 
URL = 'https://reserve.tokyodisneyresort.jp/ticket/search/'
 
def get_driver():
 
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
 
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.set_page_load_timeout(600)
    driver.implicitly_wait(1)
    driver.set_script_timeout(600)
    return driver
 
def is_bussy(driver):
    bussyMessage = driver.find_elements_by_class_name("textalign")
    if len(bussyMessage) > 0 and bussyMessage[0].text.find('アクセスが集中') != -1:
        driver.quit()
        return True
    else:
        return False
 
if __name__ == '__main__':
 
    while(True):
        driver = get_driver()
        driver.get(URL)
        if is_bussy(driver):
            time.sleep(2)
            driver.quit()
        else:
            break