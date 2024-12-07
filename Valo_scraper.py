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
    import undetected_chromedriver as uc
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
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            value = element.text
            overview.append(value)
            

        except Exception as e:
            overview.append(float("nan"))
    #Damage/Round, K/D Ratio, Headshot%, Win%
    for i in range(1,5):
        try:
            X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[{i}]/div/div[2]/span[2]/span'
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(element.text)
            overview
        except Exception as e:
            
            overview.append(float("nan"))
        
    #Winds, KAST, DDA/Round, Kills, Deaths, Assists, ACS, KAD Ratio, Kills/Round, First Blood
    for i in range(1,13):
        try:
            X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[2]/span[2]/span'
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(element.text)
            
                       #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
        except:
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[5]/div/div[1]/span[2]/span
            
            try:
                X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[1]/span[2]/span'
                element = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, X_path)))
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
    return overview

def sidebar(link,driver):
    driver.get(link)
    xpath='//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div'
    driver.implicitly_wait(3)
    elements= driver.find_elements(by='xpath', value=xpath)
    section=[]
    for i in elements:
        judul = i.text

        index=(judul.find("""\n"""))
        section.append((i.text)[0:index])

    accuracy_list = []
    roles_list = []
    top_weapons_list = []
    top_map_list=[]
    if ("Accuracy" or "Accurac") in section:
        if "Accurac" in section:
            number = section.index("Accurac")
        else:
            number = section.index("Accuracy")

        xpath_accuracy = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[{number+1}]/'
        """
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[1]

        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[1]

        """

        for row in range(1,4):    
            for col in range(1,3):
                try:
                    list_path = f'div[1]/table/tbody/tr[{row}]/td[{col}]'
                    x_path = xpath_accuracy + list_path
                    element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, x_path)))
                    accuracy_list.append(element.text)
                except:
                    accuracy_list.append(float("nan"))

    else:
        accuracy_list = [float("nan")]*6

    if "Roles" in section:
        number = section.index("Roles")
        xpath_roles = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[{number+1}]/'

        for i in range(1,5):
            path_tail = [f'div/div[{i}]/h5',f'div/div[{i}]/div[2]/div[1]/span[1]', f'div/div[{i}]/div[2]/div[1]/span[2]',
                         f'div/div[{i}]/div[2]/div[2]/span[1]', f'div/div[{i}]/div[2]/div[2]/span[2]']
            for tail in path_tail:
                try: 
                    x_path = xpath_roles+tail
                    element = driver.find_element(by='xpath', value=x_path).text
                    roles_list.append(element)
                except:
                    roles_list.append(float("nan"))
    else:
        roles_list = [float("nan")]*4*5


    if "Top Weapons" in section:
        number = section.index("Top Weapons")
        xpath_top_weapon = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[{number+1}]/div/'
        for i in range(1,4):
            path_tail = [f'div[{i}]/div[1]/div[1]',f'div[{i}]/div[1]/div[2]',
                         f'div[{i}]/div[2]/div[1]/span[1]', f'div[{i}]/div[2]/div[1]/span[2]', f'div[{i}]/div[2]/div[1]/span[3]',
                         f'div[{i}]/div[3]/span[2]']
            for tail in path_tail:
                try:
                    x_path = xpath_top_weapon+tail
                    element = driver.find_element(by='xpath', value=x_path).text
                    top_weapons_list.append(element)

                except:
                    top_weapons_list.append(float("nan"))
    else:
        top_weapons_list = [float("nan")]*3*6

    if "Top Maps" in section:
        number = section.index("Top Maps")
        xpath_top_map = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[{number+1}]/div'

        """
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{i}]/div[1] Map name
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{i}]/div[2]/div[1] Winrate
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[{i}]/div[2]/div[2] win-lose

        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[3]/div[1]
        //*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[1]/div[5]/div/div[8]/div[1]

        """
        for i in range(1,8):
            path_tail = [f'/div[{i+1}]/div[1]',
                         f'/div[{i+1}]/div[2]/div[1]',
                         f'/div[{i+1}]/div[2]/div[2]']
            for tail in path_tail:
                try:
                    x_path = xpath_top_map+tail
                    element = driver.find_element(by='xpath', value=x_path).text
                    top_map_list.append(element)
                except:
                    top_map_list.append(float("nan"))
    else:
        top_map_list = [float("nan")]*7*3
    sidebar_overview = accuracy_list+roles_list+top_weapons_list+top_map_list
    
    return sidebar_overview
