#!/usr/bin/env python
# coding: utf-8

# In[14]:


""" 
python使用3.7.6版本
webdriver使用3.14.1版本
ChromeDriver使用86.0.4240.22版本
"""
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def wait_elem(x):
    WebDriverWait(chrome,5).until(EC.presence_of_all_elements_located((By.XPATH,x)))
    return 

options=webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
options.add_argument("--headless")

chrome=webdriver.Chrome(executable_path={webdriver path},options=options)
url='https://www.youtube.com/'
chrome.get(url)
chrome.execute_script("window.scrollTo(0, document.body.scrollHeight);" )
##等待我們要的物件
wait_elem('//*[@name="search_query"]')

chrome.find_element(By.XPATH,'//*[@name="search_query"]').send_keys('學習Python - 初學者全教程')
chrome.find_element(By.XPATH,'//*[@id="search-icon-legacy"]').click()

##收尋到影片列
target = chrome.find_element_by_xpath('//*[@id="video-title"]')
chrome.execute_script("arguments[0].scrollIntoView();", target)
chrome.get(chrome.current_url)
chrome.find_element(By.XPATH,'//*[@id="video-title"]').click()
chrome.get(chrome.current_url)
##等待我們要的物件
wait_elem('//*[@id="count"]/yt-view-count-renderer/span[1]')
see_vedio=chrome.find_element(By.XPATH,'//*[@id="count"]/yt-view-count-renderer/span[1]').text
print(see_vedio)
chrome.quit()


# In[ ]:




