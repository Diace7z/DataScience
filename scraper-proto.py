#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[ ]:


def valo_scraper(series):
    for i in series:
        


# In[2]:


def link_maker(Nick):
    ID = str(Nick)
    if " " in ID:
        ID = ID.replace("\n#","#")
    hashtag = ID.find("#")
    nick = ID[:hashtag]
    tag = ID[hashtag+1:]
    link = f'https://tracker.gg/valorant/profile/riot/{nick}%23{tag}/overview'
    return link


# In[16]:


def overview(link,driver):
    driver.get(link)
    overview=[]
    
    
    #Rank, RankRating, Rank_number, Level, Match, Playtime_Hours
    list_xpath1=['//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]', #rank
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[2]', #rankrating
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[3]', #ranknumber
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span[2]', #level
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[2]', #Match
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[1]'] #Playhours
    for i in list_xpath1:

        try:
            # Tunggu sampai elemen dengan XPath tertentu muncul
            X_path = i
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            print("Elemen ditemukan:", element.text)
            value = element.text
            overview.append(value)
            print(overview)

        except Exception as e:
            print(f"Terjadi error: {e}")
            overview.append("error")
    #Damage/Round, K/D Ratio, Headshot%, Win%
    for i in range(1,5):
        X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[{i}]/div/div[2]/span[2]/span'
        value = driver.find_element(by='xpath', value=X_path).text
        overview.append(value)
        overview
        
    #Winds, KAST, DDA/Round, Kills, Deaths, Assists, ACS, KAD Ratio, Kills/Round, First Blood
    for i in range(1,13):
        try:
            X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[2]/span[2]/span'
            element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            overview.append(element.text)
            overview
            
        except:
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[5]/div/div[1]/span[2]/span
            
            try:
                X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[1]/span[2]/span'
                element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_Path)))
                overview.append(element.text)
                overview
            except:
                print("coba")

    list_xpath2=[  '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]',#RoundWin%
                   '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]', #agent1
                   '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[1]', #agent2
                   '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[5]/div[1]/div[2]/div[1]'] #agent 3
    
    for i in list_xpath2:
        try:
            X_path = i
            element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(element.text)
            print(overview)
        except:
            overview.append("error")
            print(f'{X_path}')

    for i in range(1,4): #head, body, leg
        try:
            X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[1]/div[1]/table/tbody/tr[{i}]/td[1]/span'
            element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(element.text)
            print(overview)
        except:
            overview.append("error")
            print('error di head body leg')

    for j in range(4,0,-1): #role,winrate,win,lose,kda,kill,death,assist(descending)
        list_xpath3=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/h5',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[1]/span[1]/span',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[1]/span[2]/span[1]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[1]/span[2]/span[2]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[2]/span[1]/span',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[2]/span[2]/span[1]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[2]/span[2]/span[2]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[4]/div/div[{j}]/div[2]/div[2]/span[2]/span[3]']
        for i in list_xpath3:
            X_path = i
            try:
                element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_path)))
                overview.append(element.text)
                print(overview)
            except:
                overview.append("kosong")
                print('error in role')
    for j in range(1,4):
        
        for i in list_xpath4:
                          
            
                list_xpath4=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{j}]/div[1]/div[1]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{j}]/div[2]/div/span[1]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{j}]/div[2]/div/span[2]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{j}]/div[2]/div/span[3]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{j}]/div[3]/span[2]']
                try:
                    X_path = i
                    element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, X_path)))
                    overview.append(element.text)
                    print(overview)
                except:
                    overview.append('error')
                    print(f'error di {i}')
                    
    for j in range(2,9):
        list_xpath5=[f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[6]/div/div[{j}]/div[1]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[6]/div/div[{j}]/div[2]/div[1]',
                    f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[6]/div/div[{j}]/div[2]/div[2]']
        for i in list_xpath5:
            try:
                X_path = i
                element = WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH, X_path)))
                overview.append(element.text)
                print(overview)
            except:
                overview.append('error')
                print(f'error di {i}')
    driver.quit()
    return overview


    


# In[18]:


driver = webdriver.Chrome()
driver.maximize_window()
nick = """Peggsterr#NJLTC"""
print(nick)
link = link_maker(nick)
print(link)
stats = overview('https://tracker.gg/valorant/profile/riot/poppinsguide%20com%23BUY/overview',driver)

stats


# In[16]:


stats


# In[ ]:


(/*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]/)
(/*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1])


# In[ ]:


'//*[@id=\"app\"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]/'


# In[ ]:


side bar = //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1] 
main bar = //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]


# In[ ]:


(/*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div)


# In[11]:


driver = webdriver.Chrome()
driver.maximize_window()
nick = """Peggsterr#NJLTC"""
print(nick)
link = link_maker(nick)
driver.get(link)

X_path = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div'
child_divs = driver.find_elements(By.XPATH, X_path + '/div')
print(f"Number of <div> elements: {len(child_divs)}")
print(element)


# In[9]:


# Python program to demonstrate
# selenium
 
# import webdriver
from selenium import webdriver
 
# create webdriver object
driver = webdriver.Edge()
 
# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")
driver.implicitly_wait(10) 
# get elements
elements = driver.find_elements(By.CLASS_NAME,"gsc-i-id2")
 
# print complete elements list
print(elements)

