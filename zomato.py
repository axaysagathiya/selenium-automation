from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import wget

browser = webdriver.Firefox()
targeturl = 'https://www.zomato.com/alumni-talent-directory/'
page = 1

while(True):
    
    print(' ==========>>   NEW PAGE   <<========== ')

    if page == 1:
        browser.get(targeturl)
    else:
        browser.get(targeturl + '?page=' + str(page))

    elements = browser.find_elements_by_tag_name('a')


    for elem in elements:
        href = elem.get_attribute('href')
        if re.search('.pdf$', href):
            print(href)
            wget.download(href, '/home/axay/Downloads/python/downloaded_resume/')

    page+=1
    

