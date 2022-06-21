import time

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
from selenium import webdriver
from selenium.webdriver.chrome.service import  Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# https 접속 안되는 현상 해결
context = ssl._create_unverified_context()

#네이버 거래량 상위 순위 사이트
url = "https://finance.naver.com/sise/sise_quant.naver"


with urlopen(url, context=context) as doc:
    # 인코딩을 utf-8로 하면 한글깨짐현상발생, euc-kr 로 할것
    html = BeautifulSoup(doc,'lxml',from_encoding="euc-kr")
    pgrr = html.find_all('a',class_='tltle')
    for tag in pgrr:
         print(tag.text)


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
    return driver


#driver = webdriver.Chrome('/Users/hyemin/Downloads/chromedriver')
def search_news():
    try :
        driver = set_chrome_driver()
        driver.get('https://search.naver.com/search.naver?where=news')
        time.sleep(2)

        driver.find_element(by=By.CLASS_NAME, value='box_window').click()
        elem = driver.find_element(by=By.ID,value='nx_query')
        elem.send_keys(tag.text)
        elem.send_keys(Keys.RETURN)
        elem=driver.find_element(by=By.CLASS_NAME, value='group_news')
        lis = elem.find_element(by=By.CLASS_NAME,value='bx')
        for li in lis :
            atag = li.find_element(by=By.CLASS_NAME, value='news_tit')
            print(atag.text)
            print(atag.get_attribute('href'))
            input()
    except Exception as e:
        print(e)






