def link_maker(Nick):
    ID = str(Nick)
    if " " in ID:
        ID = ID.replace(" "," %20")
    ID = ID.replace("\n#","#")
    hashtag = ID.find("#")
    nick = ID[:hashtag]
    tag = ID[hashtag+1:]
    link = f'https://tracker.gg/valorant/profile/riot/{nick}%23{tag}/overview'
    return link
def mainbar(link,driver):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    try:
        driver.get(link)
    except:
        overview=[float("nan")]*47
        pass
        
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
            X_Path = i
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            value = element.text
            overview.append(value)
            

        except Exception as e:
            overview.append(float("nan"))
    #Damage/Round, K/D Ratio, Headshot%, Win%
    for i in range(1,5):
        try:
            X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[{i}]/div/div[2]/span[2]/span'
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(value)
            overview
        except Exception as e:
            
            overview.append(float("nan"))
        
    #Winds, KAST, DDA/Round, Kills, Deaths, Assists, ACS, KAD Ratio, Kills/Round, First Blood
    for i in range(1,13):
        try:
            X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[2]/span[2]/span'
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(element.text)
            
                       #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
        except:
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[5]/div/div[1]/span[2]/span
            
            try:
                X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[1]/span[2]/span'
                element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, X_path)))
                overview.append(element.text)
                
            except Exception as e:
                
                overview.append(float("nan"))
                

    list_xpath2=['//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]']#RoundWin%]
                 
    for i in list_xpath2:
        try:
            X_path = i
            element = driver.find_element(by='xpath', value=X_Path).text
            overview.append(element.text)
            print(overview)
        except Exception as e:
            overview.append(float("nan"))
            
    
    """
    //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[{j}]/div[2]/div[1]', #agent1
    //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[3]/div[1]/div[2]/div[1]', #agent2
    //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[5]/div[1]/div[2]/div[1]'] #agent 3
    //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div
    //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[1]/
    //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[1]/div[3]/
    """
    for i in range(1,6,2):
        for j in range(1,9):
            try:
                X_path=f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[{i}]/div[{j}]'
                value = driver.find_element(by='xpath', value=X_path).text
                overview.append(value)
            except Exception as e:
                overview.append(float("nan"))
    print(overview)
    
    
    
    
    
    return overview
