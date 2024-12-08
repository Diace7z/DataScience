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
    
    
    #rank, rank_rating, rank_number, level, match, playtime_hours
    list_xpath1=['//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]', #rank
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[2]', #rankrating
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[1]/span[3]', #ranknumber
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/div/div[2]/span[2]', #level
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[2]', #Match
                '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/div/span[1]'] #Playhours
    
    #['rank','rank_rating','level', 'match', 'playtime_hours']
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
    #['damage_round','kill_death_ratio','headshot_rate','winrate']
    for i in range(1,5):
        try:
            X_path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[3]/div[{i}]/div/div[2]/span[2]/span'
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_path)))
            overview.append(element.text)
            overview
        except Exception as e:
            
            overview.append(float("nan"))
        
    #Wins, KAST, DDA/Round, Kills, Deaths, Assists, ACS, KAD Ratio, Kills/Round, First Blood
    #['win', 'kast','damage_roun','kills','death','assist','acs','kad_ratio','kill_round_ratio','first_blood','flawless_round','aces']
    for i in range(1,13):
        try:
            X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[2]/span[2]/span'
                     #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, X_Path)))
            overview.append(element.text)
            
                       #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
        except:
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/div/div[2]/span[2]/span
            #//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[5]/div/div[1]/span[2]/span
            
            try:
                X_Path = f'//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[5]/div[{i}]/div/div[1]/span[2]/span'
                element = WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH, X_Path)))
                overview.append(element.text)
                
            except Exception as e:
                
                overview.append(float("nan"))
                
    #['round_win']
    list_xpath2=['//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[2]']#RoundWin%]
                 
    for i in list_xpath2:
        try:
            X_path = i
            element = driver.find_element(by='xpath', value=X_path).text
            overview.append(element.text)
            print(overview)
        except Exception as e:
            overview.append(float("nan"))
            
    
    
    """
    ['agent1', 'matches1', 'win_rate1', 'k/d1', 'adr1', 'acs1', 'average_ddealt_round1', 'best_map1',
 'agent2', 'matches2', 'win_rate2', 'k/d2', 'adr2', 'acs2', 'average_ddealt_round2', 'best_map2',
 'agent3', 'matches3', 'win_rate3', 'k/d3', 'adr3', 'acs3', 'average_ddealt_round3', 'best_map3']
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
        #['head_rate','head_hits','body_rate','body_hits','legs_rate','legs_hits']
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
    #
    """
    ['role1', 'win_rate1', 'win_lose1', 'kda_rate1', 'kda1', 
    'role2', 'win_rate2', 'win_lose2', 'kda_rate2', 'kda2',
     'role3', 'win_rate3', 'win_lose3', 'kda_rate3', 'kda3',
     'role4', 'win_rate4', 'win_lose4', 'kda_rate4', 'kda4']
    """
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
    
    """
    ['weapon_name1', 'weapon_type1', 'head_rate1', 'body_rate1', 'legs_rate1', 'kills1',
     'weapon_name2', 'weapon_type2', 'head_rate2', 'body_rate2', 'legs_rate2', 'kills2',
     'weapon_name3', 'weapon_type3', 'head_rate3', 'body_rate3', 'legs_rate3', 'kills3']
    """
    
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
        """
        ['map_name1', 'win_rate1', 'win_lose1',
         'map_name2', 'win_rate2', 'win_lose2',
         'map_name3', 'win_rate3', 'win_lose3',
         'map_name4', 'win_rate4', 'win_lose4',
         'map_name5', 'win_rate5', 'win_lose5',
         'map_name6', 'win_rate6', 'win_lose6',
         'map_name7', 'win_rate7', 'win_lose7']
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

def id_collector(start=1, last=10,regions=["na", "eu", "ap","kr", "br", "latam"]):
    
    
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import undetected_chromedriver as uc
    import time
    import datetime
    tanggal = str(datetime.datetime.now())[:10]
    tail_name = tanggal
    for region in regions:
        table = []
        for page in range(start,last+1):
            try:
                t0 = time.time()
                driver = uc.Chrome()
                driver.maximize_window()
                driver.get("https://tracker.gg/valorant/leaderboards/ranked/pc/default?region="+region+"&page="+str(page)+"&act=dcde7346-4085-de4f-c463-2489ed47983b")
                table_XPath = '//*[@id="app"]/div[2]/div[3]/div/main/div[3]/div[2]/div/div/div[1]/div[2]/table/tbody/'
                num_rows = len(driver.find_elements(by='xpath', value=table_XPath + 'tr')) + 1
                num_cols = len(driver.find_elements(by='xpath', value=table_XPath + 'tr[1]/td'))

                for row in range(1,num_rows):
                        row_data = []
                        for col in range(1, num_cols):
                            text = driver.find_element(by='xpath', value=f'{table_XPath}tr[{row}]/td[{col}]').text
                            row_data.append(text)
                        table.append(row_data)
                print("Page "+str(page)+" on region "+region+ " Clear!")
                driver.quit()
            except:
                print("Page "+str(page)+" on region "+region+ " Failed!")
            t1 = time.time()
            print("Time Spent: ", t1-t0)
        print("Region "+region+" Clear!")
        column_name = ['ID','RankChange','RankedRating','Tier','Wins']
        df = pd.DataFrame(table)
        df.columns = column_name
       
        df.to_csv("valnames"+region+tail_name+'.csv')
        return df
