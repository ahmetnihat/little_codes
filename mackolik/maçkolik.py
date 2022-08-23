from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime


start = datetime.now()

User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
opts = Options()
opts.add_argument("user-agent=" + User_Agent)
driver = webdriver.Edge()
driver.maximize_window()
Link_Get =driver.get("http://arsiv.mackolik.com/Standings/Default.aspx?sId=54798")
time.sleep(4)

haftalik = driver.find_element_by_xpath('//*[@id="league-standing-tab"]/ul/li[8]/h3/a').click()
time.sleep(4)

driver.find_element_by_xpath('//*[@id="weekOpt"]').click()
time.sleep(0.1)
for i in range(1,35):
    driver.find_element_by_xpath('//*[@id="weekOpt"]').send_keys(Keys.ARROW_UP)
    
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="weekOpt"]').send_keys(Keys.RETURN)

with open('haftalik.txt','w'): pass
    
def listToString(s): 
    
    str1 = "" 
 
    for ele in s: 
        str1 += ele  
 
    return str1


takim = ""
def list2list(line):
    a = []
    d = []
    global takim
    parcalar = line.split(" ")
    for eleman in parcalar:
        eleman.strip(" ")
        try:
            int(eleman)
        except:
            a.append(eleman)
            
    a.pop(0)
    a.pop(0)
    a.pop(-1)
    a.pop(-1)
    
    e = a
    if len(e) == 1:
        d.append(str(e[0]))
    elif len(e) == 2:
        e = e[0] + " " + e[1]
        d.append(str(e))
    
    d = listToString(d)
    
    return d

sayma = 1
for i in range(1, 34):

    KaynakBH = driver.page_source
    # BeauBH = BeautifulSoup(KaynakBH,"html.parser")
    BeauBH = BeautifulSoup(KaynakBH)
    
    time.sleep(0.3)
    
    teams = []
    for i in range(3, 21):
        a = driver.find_element_by_xpath(f'//*[@id="league-standing-tab-body8"]/table/tbody/tr[{i}]')
        will_write = a.text + "\n"
        teams.append(will_write)
    
    
    ev_list = []
    deplasman_list = []
    score_list = []     
    
    for i in range(2, 11, 1):
        
        fixture_xpath = f'//*[@id="tblResult"]/tbody/tr[{i}]'
    
        fixture_xpath2 = fixture_xpath + "/td[4]/a"
        a1 = driver.find_element_by_xpath(fixture_xpath2).text
        
        fixture_xpath3 = fixture_xpath + "/td[6]/b/a"
        a2 = driver.find_element_by_xpath(fixture_xpath3).text
        
    
        fixture_xpath3 = fixture_xpath + "/td[8]/a"
        a3 = driver.find_element_by_xpath(fixture_xpath3).text
    
        ev_list.append(a1)
        deplasman_list.append(a3)
        score_list.append(a2)
        
    
    
    fixture_sıralama = []
    fixture_sıralama = ev_list
    fixture_sıralama.extend(deplasman_list)
    
    
    point_list = []
    d_list = []
    
    for x, line in enumerate(teams):
        if x < 18:
            d = list2list(line)
            d_list.append(d)
    
    
    
    score_list.extend(score_list)
    aralık = ["|" for i in range(1, 19)]
    hafta = [f"{sayma}. Hafta" for i in range(1, 19)]
    
    df = pd.DataFrame(columns=(f"{sayma}. Hafta","Sıralama","|","Fixture"))
    df[f"{sayma}. Hafta"] = hafta
    df["Sıralama"] = d_list
    df["|"] = aralık
    df["Fixture"] = fixture_sıralama
    df["||"] = aralık
    df["Sonuç"] = score_list
    
    df = str(df)
    Txtwrite = open('haftalik.txt','a',encoding='utf-8')
    Txtwrite.write(df)
    Txtwrite.write("\n\n\n")
    
    sayma += 1
    
    driver.find_element_by_xpath('//*[@id="weekOpt"]').click()
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="weekOpt"]').send_keys(Keys.ARROW_DOWN)
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="weekOpt"]').send_keys(Keys.RETURN)

Txtwrite.close()

finish = datetime.now()
fark = finish - start
print(fark)