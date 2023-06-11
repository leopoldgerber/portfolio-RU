#=================== LIBRARIES START ===================
from selenium.webdriver.common.action_chains import ActionChains #Для шаговых действий
from selenium.webdriver.support import expected_conditions #Чтобы input не превратился в цикл
from selenium.webdriver.support.ui import WebDriverWait #Ожидание до равенства ключа(input)
from dateutil.relativedelta import relativedelta #Для вычитания месяца
from selenium.webdriver.common.keys import Keys #Сам ключ (input)
from selenium.webdriver.common.by import By #Прописать xpath (и другие)
from selenium import webdriver #Выбрать веб драйвер (Хром)
#from itertools import islice #Оставлю, на всякий
import pandas as pd #Для датафреймов
import datetime
#import calendar
import random 
import time
import glob
import os
#=================== LIBRARIES START ===================

#=================== DEFINING FUNCTION START ===================
def get_data(first_domain, domain_amount, path, url, start, end):
    #Опции отоброжения профиля браузера
    options = webdriver.ChromeOptions()
    
    #prefs = {'download.default_directory' : 'C:\Users\Semrush\Downloads'}
    
    prefs = {"download.default_directory":r"C:\Users\Semrush\Downloads",
             "download.prompt_for_download": False,
             "download.directory_upgrade": True}
    
    options.add_experimental_option('prefs', prefs)
    #"profile.default_content_settings.popups": 0,
    
    options.add_argument("--disable-blink-features=AutomationControlled")
    #options.add_argument(r"--user-data-dir=C:\Users\Chrome\User Data\Default")
    
    #Выбор пути к драйверу (Хром) и использованные опции
    driver = webdriver.Chrome(executable_path = path, options = options)
    
    #Размер окна Хрома
    driver.set_window_size(1600,1600)
    #driver.execute_script("window.open('https://www.google.com');")

#=== ЗАПУСК ДРАЙВЕРА ============
    url = url
    driver.get(url)
    
#---Вводим данные для авторизации
    log_in_successfully = False
    while not log_in_successfully:
        try:
            try:
                time.sleep(random.randrange(2, 5, 1))
                email = WebDriverWait(driver, 
                                     random.randrange(2, 5, 1)
                                     ).until(
                                    expected_conditions.presence_of_element_located((By.ID, "email")))
                email.send_keys('login@mail.com')
                WebDriverWait(driver,
                             random.randrange(2, 5, 1)
                             ).until(lambda browser: email.get_attribute('value') == 'login@mail.com')
                print("Email input: Succeed")
            except:
                print("Email input: Failed")
            
            try:
                time.sleep(random.randrange(2, 5, 1))
                password = WebDriverWait(driver, 
                                        random.randrange(2, 5, 1)
                                        ).until(
                        expected_conditions.presence_of_element_located((By.ID, "password")))
                password.send_keys('Password')
                WebDriverWait(driver, 
                             random.randrange(2, 5, 1)
                             ).until(lambda browser: password.get_attribute('value') == 'Password')
                #button = driver.find_element("data-ui-name", "Button")
                print("Password input: Succeed")
                time.sleep(random.randrange(10, 16, 2)) 
            except:
                print("Password input: Failed")
            
            print("Log in status: Succeed")
            email.submit()
            log_in_successfully = True
            
        except:
            print("Log in status: Failed")
            log_in_successfully = False
            
#---Создание списка с выполненными доменами
    domain_list = []
    
#=== FIRST SEARCH START ============
#---Вводим DOMAIN
    time.sleep(random.randrange(4, 8, 1))
    search = driver.find_element(By.XPATH, '//*[@class="___SValue_12tss-red-team _size_l_12tss-red-team"]')
    search.send_keys(first_domain)
    WebDriverWait(driver, 
                  random.randrange(4, 8, 1)
                 ).until(lambda browser: search.get_attribute('value') == first_domain)
    search.submit()
    time.sleep(random.randrange(10, 15, 1))
    print('Demo domain sended')
    
#=== FIRST SEARCH END ============
    while len(domain_list) < domain_amount:
        time.sleep(random.randrange(2, 5, 1))
        
        if not (len(domain_list) >= domain_amount):

            domains = pd.read_csv('C:/Users/Semrush/domains.csv', sep = ';')['domain']
            domains = domains.apply(lambda x: ((str(x).replace('https://www.', '')).replace('https://', '')).replace('/', ''))
            domains = domains.drop_duplicates()
            
            for domain in domains.iloc[start:end]:
                
                print((int(end) - len(domain_list)), 'domains left')
                
                print("START:",domain)
                
#=============== SEARCHBAR START ============
                search_bar = False
                try_again = 3

                while not (try_again == 0):
                    try:        
                        cross = driver.find_element(By.XPATH, '//*[@class="srf-icon"]')
                        cross.click()

                        time.sleep(random.randrange(2, 5, 1))
                        search = driver.find_element(By.XPATH, '//*[@class="srf-searchbar__form__input js-searchbar-input"]')
                        search.send_keys(domain)
                        #print("Domain",domain,"sended")
                        time.sleep(random.randrange(2, 5, 1))

                        WebDriverWait(driver, 
                                      random.randrange(2, 5, 1)
                                     ).until(lambda browser: search.get_attribute('value') == domain)
                        search.submit()

                        print("Searachbar: Succeed")
                        try_again = 0
                        search_bar = True

                    except:
                        try:
                            #Вводим DOMAIN
                            #time.sleep(random.randrange(4, 8, 1))
                            search = driver.find_element(By.XPATH, '//*[@class="___SValue_12tss-red-team _size_l_12tss-red-team"]')
                            search.send_keys(domain)
                            WebDriverWait(driver, 
                                          random.randrange(4, 8, 1)
                                         ).until(lambda browser: search.get_attribute('value') == domain)
                            search.submit()
                            time.sleep(random.randrange(10, 15, 1))
                            print("Searachbar: Succeed")
                            try_again = 0
                            search_bar = True

                        except:
                            try_again = try_again - 1
                            print("Searachbar: Failed. Tries left:", try_again)
                        
                #print("Serachbar:",search_bar)
                
#=============== SEARCHBAR END ============
                #print("Work on the domain",domain,"has started")
                time.sleep(random.randrange(2, 5, 1))
                
                '''        
#=============== DOMAIN OVERVIEW START ===========

#---------------OVERVIEW TREND (overview-trend.xlsx)
                overview_trend = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@class="___SBody_cju2a-red-team"]//*[@class="___SButton_1gip4-red-team _size_m_1gip4-red-team _theme_secondary-muted_1gip4-red-team"]').click()
                        time.sleep(random.randrange(2, 5, 1))

                        #Нажатие на нужный CSV(semilcolon)
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi-red-team"]//div//*[@value="stdcsv"]').click()
                        time.sleep(random.randrange(2, 5, 1))

                        print("--- Overview Trend export: Succeed")
                        try_again = 0
                        overview_trend = True

                    except:
                        try_again = try_again - 1
                        print("!!! Overview Trend export: Failed. Tries left:", try_again)
                #print("Overview Trend export status:",overview_trend)


#---------------Скролл вниз
                print('Scroll')
                #print('Scroll start')
                random_number_1 = random.randrange(0, 
                                                 400, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo(0,"+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(random_number_1, 
                                                 800, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_1 = random.randrange(random_number_2, 
                                                 1200, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_2) +","+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(random_number_1, 
                                                 1600, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_1 = random.randrange(random_number_2, 
                                                 2000, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_2) +","+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(random_number_1, 
                                                 2400, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_1 = random.randrange(random_number_2, 
                                                 2800, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_2) +","+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(random_number_1, 
                                                 3200, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_2) +",3300);")
                #print("Scroll height: 3300")
                time.sleep(random.randrange(2, 4, 1))
                #print('Scroll end')

#---------------BACKLINKS (backlinks_refdomains.xlsx)          
                backlinks_refdomains = False
                try_again = 3

                while not (try_again == 0):
                    try:
                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@data-at="backlinks"]//div[3]//div[contains(@class,"___SCol_1q0t9-red-team __span_1q0t9-red-team _span_6_1q0t9-red-team")][2]//*[@class="___SButton_1gip4-red-team _size_m_1gip4-red-team _theme_secondary-muted_1gip4-red-team"]').click()
                        time.sleep(random.randrange(2, 5, 1))

                        #Нажатие на нужный CSV(semilcolon)
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi-red-team"]//div//*[@value="stdcsv"]').click()
                        time.sleep(random.randrange(2, 5, 1))

                        print("--- Backlinks Refdomains export: Succeed")
                        backlinks_refdomains_list.append(domain)
                        try_again = 0
                        backlinks_refdomains = True

                    except:
                        try_again = try_again - 1
                        print("!!! Backlinks Refdomains export: Failed. Tries left:", try_again)
                #print("Backlinks Refdomains export status:",backlinks_refdomains)

#---------------ANCHORS (backlinks_anchors.xlsx)
                backlinks_anchors = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@data-at="backlinks"]//div[3]//div[contains(@class,"___SCol_1q0t9-red-team __span_1q0t9-red-team _span_6_1q0t9-red-team")][1]//*[@class="___SButton_1gip4-red-team _size_m_1gip4-red-team _theme_secondary-muted_1gip4-red-team"]').click()
                        time.sleep(random.randrange(2, 5, 1))

                        #Нажатие на нужный CSV(semilcolon)
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi-red-team"]//div//*[@value="stdcsv"]').click()
                        time.sleep(random.randrange(2, 5, 1))

                        print("--- Backlinks Anchors export: Succeed")
                        backlinks_anchors_list.append(domain)
                        try_again = 0
                        backlinks_anchors = True

                    except:
                        try_again = try_again - 1
                        print("!!! Backlinks Anchors export: Failed. Tries left:", try_again)
                #print("Backlinks Anchors export status:",backlinks_anchors)

#---------------Скролл вверх
                print('Scroll')
                #print('Scroll start')
                random_number_1 = random.randrange(2800, 
                                                 3300, 
                                                 random.randrange(50, 
                                                                  200, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo(3300,"+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(2200, 
                                                 random_number_1, 
                                                 random.randrange(50, 
                                                                  200, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_1 = random.randrange(1600, 
                                                 random_number_2, 
                                                 random.randrange(50, 
                                                                  200, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_2) +","+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(1000, 
                                                 random_number_1, 
                                                 random.randrange(50, 
                                                                  200, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_1 = random.randrange(400, 
                                                 random_number_2, 
                                                 random.randrange(50, 
                                                                  200, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_2) +","+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                #time.sleep(random.randrange(2, 4, 1))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +",0);")
                #print("Scroll height:","0")
                time.sleep(random.randrange(2, 4, 1))
                #print('Scroll end')
                '''

#---------------Navigation
                export = driver.find_element(By.XPATH, '//*[@id="srf-sidebar"]//div[contains(@class,"srf-report-sidebar-main__group js-sidebar-group")]//div[contains(@id,"accordion-content-seo")]//a[contains(@data-test,"seo_traffic_analytics")]').click()
                time.sleep(random.randrange(5, 8, 1))
                print("Change page: Traffic Analytics")
            
#=============== DOMAIN OVERVIEW END ===========

#=============== TRAFFIC ANALYTICS START =========== 

#---------------TREND BY DEVICE !VISITS!(Trend By Devices.xlsx)
                visits = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SBoxInline_8om4t_gg_ ___SButton_1gip4_gg_ _size_m_1gip4_gg_ _size_m_wus9c_gg_ _theme_secondary-muted_1gip4_gg_"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на нужный CSV
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi_gg_"]//div//div[contains(@class,"___SDropdownMenuItem_wus9c_gg_ _size_m_wus9c_gg_ ___SFlex_3onux_gg_")][2]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        print("--- Visits: Succeed")
                        visits_list.append(domain)
                        try_again = 0
                        visits = True

                    except:
                        try_again = try_again - 1
                        print("!!! Visits: Failed. Tries left:", try_again)
                #print("Visits status:",visits)
                
#---------------TREND BY DEVICE !UNIQUE! (Trend By Devices.xlsx)
                unique = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку UNIQUE
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SPills_b6lww_gg_ _size_m_b6lww_gg_"]//button[@value="users"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SBoxInline_8om4t_gg_ ___SButton_1gip4_gg_ _size_m_1gip4_gg_ _size_m_wus9c_gg_ _theme_secondary-muted_1gip4_gg_"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на нужный CSV
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi_gg_"]//div//div[contains(@class,"___SDropdownMenuItem_wus9c_gg_ _size_m_wus9c_gg_ ___SFlex_3onux_gg_")][2]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        print("--- Unique export: Succeed")
                        unique_list.append(domain)
                        try_again = 0
                        unique = True

                    except:
                        try_again = try_again - 1
                        print("!!! Unique export: Failed. Tries left:", try_again)
                #print("Unique status:",unique)

#---------------TREND BY DEVICE !DURATION! (Trend By Devices.xlsx)
                duration = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку DURATION
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SPills_b6lww_gg_ _size_m_b6lww_gg_"]//button[@value="time_on_site"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SBoxInline_8om4t_gg_ ___SButton_1gip4_gg_ _size_m_1gip4_gg_ _size_m_wus9c_gg_ _theme_secondary-muted_1gip4_gg_"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на нужный CSV
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi_gg_"]//div//div[contains(@class,"___SDropdownMenuItem_wus9c_gg_ _size_m_wus9c_gg_ ___SFlex_3onux_gg_")][2]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        print("--- Duration export: Succeed")
                        duration_list.append(domain)
                        try_again = 0
                        duration = True

                    except:
                        try_again = try_again - 1
                        print("!!! Duration export: Failed. Tries left:", try_again)
                #print("Duration status:",duration)
                
#---------------TREND BY DEVICE !BOUNCE RATE! (Trend By Devices.xlsx)
                bounce_rate = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку BOUNCE RATE
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SPills_b6lww_gg_ _size_m_b6lww_gg_"]//button[@value="bounce_rate"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SBoxInline_8om4t_gg_ ___SButton_1gip4_gg_ _size_m_1gip4_gg_ _size_m_wus9c_gg_ _theme_secondary-muted_1gip4_gg_"]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на нужный CSV
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi_gg_"]//div//div[contains(@class,"___SDropdownMenuItem_wus9c_gg_ _size_m_wus9c_gg_ ___SFlex_3onux_gg_")][2]').click()
                        #time.sleep(random.randrange(2, 5, 1))
                        time.sleep(random.randrange(1, 4, 1))

                        print("--- Bounce Rate export: Succeed")
                        bounce_rate_list.append(domain)
                        try_again = 0
                        bounce_rate = True

                    except:
                        try_again = try_again - 1
                        print("!!! Bounce Rate export: Failed. Tries left:", try_again)
                #print("Bounce Rate status:",bounce_rate)

#---------------Скролл вниз
                #print('Scroll')
                #print('Scroll start')
                random_number_1 = random.randrange(0, 
                                                 400, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo(0,"+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(random_number_1, 
                                                 800, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                time.sleep(random.randrange(1, 4, 1))
                random_number_1 = random.randrange(random_number_2, 
                                                 1100, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +",1100);")
                #print("Scroll height: 1100")
                time.sleep(random.randrange(1, 4, 1))
                #print('Scroll end')
                                
#---------------TRAFFIC SOURCES (Traffic Sources by Type.xlsx)
                traffic_sources = False
                try_again = 3

                while not (try_again == 0):
                    try:

                        #Нажатие на кнопку ЭКСПОРТ
                        export = driver.find_element(By.XPATH, '//div[contains(@class,"sc-1h9cu94-0 hSKyfN")]//button[contains(@class, "___SBoxInline_8om4t_gg_ ___SButton_1gip4_gg_ _size_m_1gip4_gg_ _size_m_wus9c_gg_ _theme_secondary-muted_1gip4_gg_")]').click()
                        time.sleep(random.randrange(1, 4, 1))

                        #Нажатие на нужный CSV
                        csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi_gg_"]//div//div[contains(@class,"___SDropdownMenuItem_wus9c_gg_ _size_m_wus9c_gg_ ___SFlex_3onux_gg_")][2]').click()
                        time.sleep(random.randrange(1, 4, 1))

                        print("--- Traffic Sources by Type export: Succeed")
                        traffic_sources_list.append(domain)
                        try_again = 0
                        traffic_sources = True

                    except:
                        try_again = try_again - 1
                        print("!!! Traffic Sources by Type export: Failed. Tries left:", try_again)
                #print("Traffic Sources by Type export status:",traffic_sources)  

#---------------Скролл вверх
                #print('Scroll')
                #print('Scroll start')
                random_number_1 = random.randrange(800, 
                                                 1100, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo(1100, "+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(400, 
                                                 random_number_1, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                time.sleep(random.randrange(1, 4, 1))
                random_number_1 = random.randrange(0, 
                                                 random_number_2, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +",0);")
                #print("Scroll height: 0")
                time.sleep(random.randrange(1, 4, 1))
                #print('Scroll end')
                
#---------------Navigation
                export = driver.find_element(By.XPATH, '//*[@class="sc-1bc4zew-0 ccJnmu"]//div[contains(@class,"___STabLine_nxhjn_gg_ __underlined_nxhjn_gg_ _size_m_nxhjn_gg_")]//button[contains(@data-test,"reportTab journey")]').click()
                time.sleep(random.randrange(5, 8, 1))
                print("Change menu link: Traffic Analytics:Journey")
                
#=============== TRAFFIC JOURNEY START ============
            
#---------------TRAFFIC JOURNEY  (All sources.xlsx)
                for x in month_list:
                    
                    
                    traffic_by_countries_2 = False
                    try_again = 3

                    while not (try_again == 0):
                        try:

                            #Нажатие на кнопку 
                            export = driver.find_element(By.XPATH, '//a[@data-ui-name="MonthRangePicker.Trigger"]').click()
                            time.sleep(random.randrange(1, 4, 1))

                            #Нажатие на кнопку 
                            export = driver.find_element(By.XPATH, '//button[@aria-label="'+x+' 1, 2022"]').click()
                            time.sleep(random.randrange(1, 4, 1))

                            #Нажатие на кнопку 
                            export = driver.find_element(By.XPATH, '//div[@data-ui-name="Dropdown.Popper"]//button[@data-test="selector-apply"]').click()
                            time.sleep(random.randrange(1, 4, 1))

                            #---------------Скролл вниз
                            #print('Scroll')
                            #print('Scroll start')
                            random_number_1 = random.randrange(0, 
                                                             300, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo(0,"+ str(random_number_1) +");")
                            #print("Scroll height:",random_number_1)
                            #time.sleep(random.randrange(2, 4, 1))
                            random_number_2 = random.randrange(random_number_1, 
                                                             500, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                            #print("Scroll height:",random_number_2)
                            time.sleep(random.randrange(1, 4, 1))
                            random_number_1 = random.randrange(random_number_2, 
                                                             900, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +",1100);")
                            #print("Scroll height: 1100")
                            time.sleep(random.randrange(1, 4, 1))
                            #print('Scroll end')
                            
                            
                            #---------------TRAFFIC JOURNEY (All Sources.xlsx)
                            journey = False
                            try_again = 3

                            while not (try_again == 0):
                                try:

                                    #Нажатие на кнопку CSV
                                    export = driver.find_element(By.XPATH, '//button[contains(@data-test, "csv-button")]').click()
                                    time.sleep(random.randrange(1, 4, 1))

                                    print("--- Journey export: Succeed")
                                    globals()['journey_list_%s' % x].append(domain)
                                    try_again = 0
                                    journey = True

                                except:
                                    try_again = try_again - 1
                                    print("!!! Journey: Failed. Tries left:", try_again)
                            #print("Journey status:",journey)  

                            #---------------Скролл вверх
                            #print('Scroll')
                            #print('Scroll start')
                            random_number_1 = random.randrange(500, 
                                                             900, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo(1100, "+ str(random_number_1) +");")
                            #print("Scroll height:",random_number_1)
                            #time.sleep(random.randrange(2, 4, 1))
                            random_number_2 = random.randrange(300, 
                                                             random_number_1, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                            #print("Scroll height:",random_number_2)
                            time.sleep(random.randrange(1, 4, 1))
                            random_number_1 = random.randrange(0, 
                                                             random_number_2, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +",0);")
                            #print("Scroll height: 0")
                            time.sleep(random.randrange(2, 4, 1))
                            #print('Scroll end')

                            print("--- Month "+x+" changed: Succeed")
                            journey_list.append(domain)
                            try_again = 0
                            traffic_by_countries_2 = True

                        except:
                            try_again = try_again - 1
                            print("!!! Month changed: Failed. Tries left:", try_again)
                #print("traffic_by_countries_2 status:",traffic_by_countries_2)

#---------------Navigation
                export = driver.find_element(By.XPATH, '//*[@class="sc-1bc4zew-0 ccJnmu"]//div[contains(@class,"___STabLine_nxhjn_gg_ __underlined_nxhjn_gg_ _size_m_nxhjn_gg_")]//button[contains(@data-test,"reportTab geo")]').click()
                time.sleep(random.randrange(5, 8, 1))
                print("Change menu link: Traffic Analytics:Geo Distribution")
                
#=============== TRAFFIC SOURCE END ============
                
#=============== TRAFFIC GEO DISTRIBUTION START ============
            
#---------------TRAFFIC COUNTRIES  (Traffic by Country.xlsx)
                for x in month_list:
                    
                    
                    traffic_by_countries_2 = False
                    try_again = 3

                    while not (try_again == 0):
                        try:

                            #Нажатие на кнопку 
                            export = driver.find_element(By.XPATH, '//a[@data-ui-name="MonthRangePicker.Trigger"]').click()
                            time.sleep(random.randrange(1, 4, 1))

                            #Нажатие на кнопку 
                            export = driver.find_element(By.XPATH, '//button[@aria-label="'+x+' 1, 2022"]').click()
                            time.sleep(random.randrange(1, 4, 1))

                            #Нажатие на кнопку 
                            export = driver.find_element(By.XPATH, '//div[@data-ui-name="Dropdown.Popper"]//button[@data-test="selector-apply"]').click()
                            time.sleep(random.randrange(1, 4, 1))

                            #---------------Скролл вниз
                            #print('Scroll')
                            random_number_1 = random.randrange(0, 
                                                             300, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo(0,"+ str(random_number_1) +");")
                            time.sleep(random.randrange(1, 4, 1))
                            random_number_2 = random.randrange(random_number_1, 
                                                             500, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                            time.sleep(random.randrange(1, 4, 1))
                            random_number_1 = random.randrange(random_number_2, 
                                                             900, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +",1100);")
                            time.sleep(random.randrange(1, 4, 1))

                            #---------------TRAFFIC SOURCES (Trend By Countries.xlsx)
                            trend_countries = False
                            try_again = 3

                            while not (try_again == 0):
                                try:

                                    #Нажатие на кнопку CSV
                                    export = driver.find_element(By.XPATH, '//div[contains(@data-test,"geoDistributionList")]//button[contains(@class, "___SButton_1gip4_gg_ _size_m_1gip4_gg_ _theme_secondary-muted_1gip4_gg_")]').click()
                                    time.sleep(random.randrange(1, 4, 1))

                                    print("--- Trend By Countries export: Succeed")
                                    #traffic_by_countries_list.append(domain)
                                    globals()['traffic_by_countries_list_%s' % x].append(domain)
                                    try_again = 0
                                    trend_countries = True

                                except:
                                    try_again = try_again - 1
                                    print("!!! Trend By Countries export: Failed. Tries left:", try_again)

                            #---------------Скролл вверх
                            #print('Scroll')
                            random_number_1 = random.randrange(500, 
                                                             900, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo(1100, "+ str(random_number_1) +");")
                            time.sleep(random.randrange(1, 4, 1))
                            random_number_2 = random.randrange(300, 
                                                             random_number_1, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                            time.sleep(random.randrange(1, 4, 1))
                            random_number_1 = random.randrange(0, 
                                                             random_number_2, 
                                                             random.randrange(50, 
                                                                              100, 
                                                                              random.randrange(10, 25, 4)))
                            driver.execute_script("window.scrollTo("+ str(random_number_1) +",0);")
                            time.sleep(random.randrange(1, 4, 1))

                            print("--- Month "+x+" changed: Succeed")
                            traffic_by_countries_list.append(domain)
                            try_again = 0
                            traffic_by_countries_2 = True

                        except:
                            try_again = try_again - 1
                            print("!!! Month "+x+" changed: Failed. Tries left:", try_again)
                #print("traffic_by_countries_2 status:",traffic_by_countries_2)

#---------------Скролл вверх
                #print('Scroll')
                #print('Scroll start')
                random_number_1 = random.randrange(500, 
                                                 900, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo(1100, "+ str(random_number_1) +");")
                #print("Scroll height:",random_number_1)
                #time.sleep(random.randrange(2, 4, 1))
                random_number_2 = random.randrange(300, 
                                                 random_number_1, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +","+ str(random_number_2) +");")
                #print("Scroll height:",random_number_2)
                time.sleep(random.randrange(1, 4, 1))
                random_number_1 = random.randrange(0, 
                                                 random_number_2, 
                                                 random.randrange(50, 
                                                                  100, 
                                                                  random.randrange(10, 25, 4)))
                driver.execute_script("window.scrollTo("+ str(random_number_1) +",0);")
                #print("Scroll height: 0")
                time.sleep(random.randrange(1, 4, 1))
                #print('Scroll end')
                
#====================== TRAFFIC GEO DISTRIBUTION END ============

#====================== TRAFFIC ANALYTICS END =========== 

#---------------Navigation
                export = driver.find_element(By.XPATH, '//*[@id="srf-sidebar"]//div[contains(@class,"srf-report-sidebar-main__group js-sidebar-group")]//div[contains(@id,"accordion-content-seo")]//a[contains(@data-test,"seo_domain_overview")]').click()
                time.sleep(random.randrange(5, 8, 1))
                print("Change page: Domain Overview")

#====================== STATUS ALERT START =========== 
                #Оповещение об окончании скачивании файлов для домена
                print("END:",domain)
                time.sleep(random.randrange(1, 4, 1))

                #Добавляем к списку выполненный домен
                domain_list.append(domain)
                #print("Domain",domain,"added in domain_list.")
#====================== STATUS ALERT END =========== 

#=================== DEFINING FUNCTION END ===================

#=================== OVERVIEW START ===================
def overview():
    temp = []
    pd_path = downloads_path+'Overview'
    csv_files = glob.glob(os.path.join(path, "*.csv"))

    for f in csv_files:
        i = f.split("\\")[-1]
        #print(cut)
        df = pd.read_csv(pd_path+i, sep = ';')
        df.columns = df.columns.str.lower()
        temp.append(df)

    overview = pd.concat(temp, axis = 0, ignore_index = True)

    #Save as Excel
    overview_path = output_path+'overview.xlsx'
    writer = pd.ExcelWriter(overview_path,engine='xlsxwriter')
    data = overview.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
#=================== OVERVIEW START ===================

#=================== BACKLINKS ANCHORS START ===================
def backlinks_anchors():
    temp = []

    for i in backlinks_anchors_list:
        filename = downloads_path+i+'-backlinks_anchors.csv'
        df = pd.read_csv(filename, sep = ";")
        #df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df['Domain'] = i
        df.columns = df.columns.str.lower()
        temp.append(df)

    backlinks_anchors = pd.concat(temp, axis = 0, ignore_index = True)
    backlinks_anchors = pd.merge(backlinks_anchors, domains,on="domain",how="left")
    
    #Save as Excel
    backlinks_anchors_path = output_path+'backlinks_anchors.xlsx'
    writer = pd.ExcelWriter(backlinks_anchors_path,engine='xlsxwriter')
    data = backlinks_anchors.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
#=================== BACKLINKS ANCHORS END ===================

#=================== BACKLINKS REFDOMAINS START ===================    
def backlinks_refdomains():
    temp = []

    for i in backlinks_refdomains_list:
        filename = downloads_path+i+'-backlinks_refdomains.csv'
        df = pd.read_csv(filename, sep = ";")
        #df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df['Domain'] = i
        df.columns = df.columns.str.lower()
        temp.append(df)

    backlinks_refdomains = pd.concat(temp, axis = 0, ignore_index = True)
    backlinks_refdomains.fillna(0, inplace = True)
    
    backlinks_refdomains = pd.merge(backlinks_refdomains, domains,on="domain",how="left")

    #Save as Excel
    backlinks_refdomains_path = output_path+'backlinks_refdomains.xlsx'
    writer = pd.ExcelWriter(backlinks_refdomains_path,engine='xlsxwriter')
    data = backlinks_refdomains.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
#=================== BACKLINKS REFDOMAINS END ===================

#=================== TREND BY DEVICES START ===================
def trend_by_devices():
    visits_temp = []
    unique_temp = []
    duration_temp = []
    bounce_temp = []
    
    #first_month = (datetime.date.today() - relativedelta(months=6)).strftime('%b')
    #last_month = datetime.date.today().strftime('%b')
    first_month = 'Mar'
    last_month = 'Sep'
    year = datetime.date.today().strftime('%Y')

    for i in visits_list:
        filename = downloads_path+'Trend By Devices (domain='+i+', metric=visits, range='+first_month+' – '+last_month+' '+year+', devices=all_devices,desktop,mobile).csv'
        df_visits = pd.read_csv(filename, sep = ",")
        df_visits.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df_visits['Domain'] = i
        df_visits.columns = df_visits.columns.str.lower()
        visits_temp.append(df_visits)
        
    for i in unique_list:
        filename = downloads_path+'Trend By Devices (domain='+i+', metric=users, range='+first_month+' – '+last_month+' '+year+', devices=all_devices,desktop,mobile).csv'
        df_unique = pd.read_csv(filename, sep = ",")
        df_unique.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df_unique['Domain'] = i
        df_unique.columns = df_unique.columns.str.lower()
        unique_temp.append(df_unique)
        
    for i in duration_list:
        filename = downloads_path+'Trend By Devices (domain='+i+', metric=time_on_site, range='+first_month+' – '+last_month+' '+year+', devices=all_devices,desktop,mobile).csv'
        df_duration = pd.read_csv(filename, sep = ",")
        df_duration.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df_duration['Domain'] = i
        df_duration.columns = df_duration.columns.str.lower()
        duration_temp.append(df_duration)

    for i in bounce_rate_list:
        filename = downloads_path+'Trend By Devices (domain='+i+', metric=bounce_rate, range='+first_month+' – '+last_month+' '+year+', devices=all_devices,desktop,mobile).csv'
        df_bounce = pd.read_csv(filename, sep = ",")
        df_bounce.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df_bounce['Domain'] = i
        df_bounce.columns = df_bounce.columns.str.lower()
        bounce_temp.append(df_bounce)

    visits = pd.concat(visits_temp, axis = 0, ignore_index = True)
    visits.fillna(0, inplace = True)
    visits.rename(columns = {'all devices':'visits_devices', 'desktop':'visits_desktop','mobile':'visits_mobile'}, inplace = True)

    unique = pd.concat(unique_temp, axis = 0, ignore_index = True)
    unique.fillna(0, inplace = True)
    unique.rename(columns = {'all devices':'unique_devices', 'desktop':'unique_desktop','mobile':'unique_mobile'}, inplace = True)

    duration = pd.concat(duration_temp, axis = 0, ignore_index = True)
    duration.fillna(0, inplace = True)
    duration.rename(columns = {'all devices':'duration_devices', 'desktop':'duration_desktop','mobile':'duration_mobile'}, inplace = True)

    bounce = pd.concat(bounce_temp, axis = 0, ignore_index = True)
    bounce.fillna(0, inplace = True)
    bounce.rename(columns = {'all devices':'bounce_devices', 'desktop':'bounce_desktop','mobile':'bounce_mobile'}, inplace = True)

    trend_by_devices = pd.merge(visits, bounce, how='left', on = ['month', 'domain'])
    trend_by_devices = pd.merge(trend_by_devices, unique, how='left', on = ['month', 'domain'])
    trend_by_devices = pd.merge(trend_by_devices, duration, how='left', on = ['month', 'domain'])

    # bounce_all
    trend_by_devices['all_no_bounce'] = round((trend_by_devices['visits_devices'] * trend_by_devices['bounce_devices']).astype(float))
    trend_by_devices['all_bounce'] = round((trend_by_devices['visits_devices'] - (trend_by_devices['visits_devices'] * trend_by_devices['bounce_devices'])).astype(float))

    # bounce_desktop
    trend_by_devices['desktop_no_bounce'] = round((trend_by_devices['visits_desktop'] * trend_by_devices['bounce_desktop']).astype(float))
    trend_by_devices['desktop_bounce'] = round((trend_by_devices['visits_desktop'] - (trend_by_devices['visits_desktop'] * trend_by_devices['bounce_desktop'])).astype(float))

    # bounce_mobile
    trend_by_devices['mobile_no_bounce'] = round((trend_by_devices['visits_mobile'] * trend_by_devices['bounce_mobile']).astype(float))
    trend_by_devices['mobile_bounce'] = round((trend_by_devices['visits_mobile'] - (trend_by_devices['visits_mobile'] * trend_by_devices['bounce_mobile'])).astype(float))
    
    trend_by_devices = pd.merge(trend_by_devices, domains,on="domain",how="left")
    
    #Month = Mon + Year
    trend_by_devices['year'] = (pd.DatetimeIndex(trend_by_devices['month']).year).astype("string")
    
    trend_by_devices['month'] = trend_by_devices['month_number'] = pd.DatetimeIndex(trend_by_devices['month']).month
    trend_by_devices['month_number'] = trend_by_devices['month_number'].astype("string")
    trend_by_devices['month'] = trend_by_devices['month_number'].apply(lambda x: (datetime.datetime.strptime(x, "%m")).strftime("%b"))
    
    #trend_by_devices['month'] = trend_by_devices['month'].apply(lambda x: calendar.month_abbr[x])
    #trend_by_devices['month_number'] = trend_by_devices['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)
    
    trend_by_devices['month_year'] = (pd.to_datetime(trend_by_devices['month_number'] + ' ' + trend_by_devices['year'])).dt.strftime('%d.%m.%Y')
    
    #trend_by_devices['month_year'] = pd.to_datetime(trend_by_devices['month_year'])
    #trend_by_devices['month_year'] = trend_by_devices['month_year'].dt.strftime('%d.%m.%Y')
        
    #Save as Excel
    trend_by_devices_path = output_path+'trend_by_devices.xlsx'
    writer = pd.ExcelWriter(trend_by_devices_path,engine='xlsxwriter')
    data = trend_by_devices.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
#=================== TREND BY DEVICES END ===================

#=================== TRAFFIC SOURCES START ===================
def traffic_sources():
    temp = []
    
    #first_month = (datetime.date.today() - relativedelta(months=6)).strftime('%b')
    #last_month = datetime.date.today().strftime('%b')
    first_month = 'Mar'
    last_month = 'Sep'
    year = datetime.date.today().strftime('%Y')

    for i in traffic_sources_list:
        filename = downloads_path+'Traffic Sources by Type (domain='+i+', range='+first_month+' '+year+' – '+last_month+' '+year+').csv'
        df = pd.read_csv(filename, sep = ",")
        df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
        df['Domain'] = i
        df.columns = df.columns.str.lower()
        temp.append(df)

    traffic_sources = pd.concat(temp, axis = 0, ignore_index = True)
    traffic_sources.fillna(0, inplace = True)
    
    traffic_sources = pd.merge(traffic_sources, domains,on="domain",how="left")
    
    #Month = Mon + Year
    traffic_sources['year'] = (pd.DatetimeIndex(traffic_sources['month']).year).astype("string")
    
    traffic_sources['month'] = traffic_sources['month_number'] = pd.DatetimeIndex(traffic_sources['month']).month
    traffic_sources['month_number'] = traffic_sources['month_number'].astype("string")
    traffic_sources['month'] = traffic_sources['month_number'].apply(lambda x: (datetime.datetime.strptime(x, "%m")).strftime("%b"))
    
    #traffic_sources['month'] = traffic_sources['month'].apply(lambda x: calendar.month_abbr[x])
    #traffic_sources['month_number'] = traffic_sources['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)
    
    traffic_sources['month_year'] = (pd.to_datetime(traffic_sources['month_number'] + ' ' + traffic_sources['year'])).dt.strftime('%d.%m.%Y')
    
    #traffic_sources['month_year'] = pd.to_datetime(traffic_sources['month_year'])
    #traffic_sources['month_year'] = traffic_sources['month_year'].dt.strftime('%d.%m.%Y')
    
    #Save as Excel
    traffic_sources_path = output_path+'traffic_sources.xlsx'
    writer = pd.ExcelWriter(traffic_sources_path,engine='xlsxwriter')
    data = traffic_sources.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
#=================== TRAFFIC SOURCES END ===================

#=================== JOURNEY SOURCES START ===================
def journey_sources():
    temp_count = 1
    journey_temp = []
    
    for x in month_list:
        #domains = pd.read_csv('C:/Users/gerber.l/Downloads/domains.csv', sep = ';')

        last_month = (datetime.date.today() - relativedelta(months=temp_count+1)).strftime('%b')
        #last_month = 'Aug'
        year = datetime.date.today().strftime('%Y')

        for i in globals()['journey_list_%s' % x]:
            filename = downloads_path+'All Sources (date='+last_month+' '+year+', target='+i+').csv'
            df = pd.read_csv(filename, sep = ",")
            #df.rename(columns = {'Unnamed: 0':'Month'}, inplace = True)
            df.columns = df.columns.str.lower()
            df['domain'] = i
            df['month'] = x
            df['year'] = year
            journey_temp.append(df)

        temp_count += 1

    journey_sources = pd.concat(journey_temp, axis = 0, ignore_index = True)
    journey_sources.fillna(0, inplace = True)

    journey_sources = pd.merge(journey_sources, domains,on="domain",how="left")
        
    #Month = Mon
    journey_sources['year'] = journey_sources['year'].astype("string")
    
    journey_sources['month_number'] = journey_sources['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)
    journey_sources['month_number'] = journey_sources['month_number'].astype("string")
    journey_sources['month_year'] = (pd.to_datetime(journey_sources['month_number'] + ' ' + journey_sources['year'])).dt.strftime('%d.%m.%Y')
    
    #Save as Excel
    journey_sources_path = output_path+'journey_sources.xlsx'
    writer = pd.ExcelWriter(journey_sources_path,engine='xlsxwriter')
    data = journey_sources.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
#=================== JOURNEY SOURCES END ===================

#=================== TRAFFIC BY COUNTRIES START ===================
def traffic_by_countries(end, month_list): 
    countries = pd.read_csv('C:/Users/semrush files/countries.csv', engine="python", encoding="cp1251", sep=';', quotechar='"', error_bad_lines=False)
    countries.rename(columns = {'short':'country'}, inplace = True)
    
    temp_count = 1
    traffic_temp = []

    for x in month_list:
        #domains = pd.read_csv('C:/Users/Downloads/domains.csv', sep = ';')

        last_month = (datetime.date.today() - relativedelta(months=temp_count+1)).strftime('%b')
        #last_month = 'Aug'
        year = datetime.date.today().strftime('%Y')

        traffic_1 = pd.read_csv(downloads_path+'Traffic by Country (date='+str(last_month)+' '+str(year)+', geoType=country).csv', sep = '","|""|,|"')
        traffic_1 = traffic_1[traffic_1.columns.drop(list(traffic_1.filter(regex='Unnamed')))]
        traffic_1.columns = traffic_1.columns.str.lower()
        traffic_1['domain'] = globals()['traffic_by_countries_list_%s' % x][0]
        traffic_1['month'] = x
        traffic_1['year'] = year
        traffic_temp.append(traffic_1)

        for i in range(1, end):
            traffic_by_countries_name = downloads_path+'Traffic by Country (date='+str(last_month)+' '+str(year)+', geoType=country) ('+str(i)+').csv'
            traffic_by_countries = pd.read_csv(traffic_by_countries_name, sep = '","|""|,|"')
            traffic_by_countries = traffic_by_countries[traffic_by_countries.columns.drop(list(traffic_by_countries.filter(regex='Unnamed')))]
            traffic_by_countries['Domain'] = globals()['traffic_by_countries_list_%s' % x][i]
            traffic_by_countries['Month'] = x
            traffic_by_countries['Year'] = year
            traffic_by_countries.columns = traffic_by_countries.columns.str.lower()
            traffic_temp.append(traffic_by_countries)

        temp_count += 1

    traffic_concat = pd.concat(traffic_temp, axis = 0, ignore_index = True)   

    traffic_countries = pd.merge(traffic_concat, countries,on="country",how="left")
    traffic_countries['bounce rate'] = traffic_countries['bounce rate'].str.rstrip("%").astype(float)

    traffic_countries['traffic_no_bounce'] = round((traffic_countries['traffic'] - ((traffic_countries['traffic'] * traffic_countries['bounce rate']) / 100)).astype(float))
    traffic_countries['traffic_bounce'] = round(((traffic_countries['traffic'] * traffic_countries['bounce rate']) / 100).astype(float))

    traffic_countries['desktop share'] = traffic_countries['desktop share'].apply(lambda x : '0%' if str(x) == '<\xa00.01%' else x)
    traffic_countries['mobile share'] = traffic_countries['mobile share'].apply(lambda x : '0%' if str(x) == '<\xa00.01%' else x)

    traffic_countries['desktop share'] = traffic_countries['desktop share'].str.rstrip("%").astype(float)
    traffic_countries['mobile share'] = traffic_countries['mobile share'].str.rstrip("%").astype(float)

    traffic_countries['desktop'] = round(((traffic_countries['unique visitors'] * traffic_countries['desktop share']) / 100).astype(float))
    traffic_countries['mobile'] = round(((traffic_countries['unique visitors'] * traffic_countries['mobile share']) / 100).astype(float))

    traffic_countries = pd.merge(traffic_countries, domains,on="domain",how="left")
    
    #Month = Mon
    traffic_countries['year'] = traffic_countries['year'].astype("string")
    traffic_countries['month_number'] = traffic_countries['month'] = traffic_countries['month'].apply(lambda x: datetime.datetime.strptime(x, "%b").month)
    traffic_countries['month_number'] = traffic_countries['month_number'].astype("string")
    traffic_countries['month'] = traffic_countries['month_number'].apply(lambda x: (datetime.datetime.strptime(x, "%m")).strftime("%b"))
    #traffic_countries['month'] = traffic_countries['month'].apply(lambda x: calendar.month_abbr[x])
    
    traffic_countries['month_year'] = (pd.to_datetime(traffic_countries['month_number'] + ' ' + traffic_countries['year'])).dt.strftime('%d.%m.%Y')
    
    countries_ru_list = traffic_countries['name'].drop_duplicates()
    countries_en_list = traffic_countries['english'].drop_duplicates()
    countries_location_ru_list = traffic_countries['location'].drop_duplicates()
    calendar = traffic_countries['month_year'].drop_duplicates()
    
    #Save as Excel (traffic_countries)
    traffic_countries_path = output_path+'traffic_countries.xlsx'
    writer = pd.ExcelWriter(traffic_countries_path,engine='xlsxwriter')
    data = traffic_countries.to_excel(writer, sheet_name = 'Лист 1', index = False)
    writer.save()
    
    #Save as Excel (countries_ru_list)
    countries_ru_path = output_path+'countries_ru_list.xlsx'
    writer = pd.ExcelWriter(countries_ru_path,engine='xlsxwriter')
    data = countries_ru_list.to_excel(writer, sheet_name = 'Лист 1', index = True)
    writer.save()

    #Save as Excel (countries_en_list)
    countries_en_path = output_path+'countries_en_list.xlsx'
    writer = pd.ExcelWriter(countries_en_path,engine='xlsxwriter')
    data = countries_en_list.to_excel(writer, sheet_name = 'Лист 1', index = True)
    writer.save()

    #Save as Excel (countries_location_ru_list)
    countries_location_ru_path = output_path+'countries_location_ru_list.xlsx'
    writer = pd.ExcelWriter(countries_location_ru_path,engine='xlsxwriter')
    data = countries_location_ru_list.to_excel(writer, sheet_name = 'Лист 1', index = True)
    writer.save()
    
    #Save as Excel (calendar)
    calendar_output_path = output_path+'calendar.xlsx'
    writer = pd.ExcelWriter(calendar_output_path,engine='xlsxwriter')
    data = calendar.to_excel(writer, sheet_name = 'Лист 1', index = True)
    writer.save()
#=================== TRAFFIC BY COUNTRIES END ===================

#=================== COMPANY & DOMAINS START ===================
def domains_company(start, end):
    domains = pd.read_csv('C:/Users/Semrush/domains.csv', sep = ';')
    domains['domain'] = domains['domain'].apply(lambda x: ((str(x).replace('https://www.', '')).replace('https://', '')).replace('/', ''))
    domains = domains.drop_duplicates()
    company = domains['company'].drop_duplicates()
    domains = domains['domain']

    temp_domains = domains.loc[start:(end - 1)]
    temp_company = company.loc[start:(end - 1)]

    #Save as Excel
    domains_list_path = output_path+'domains_list.xlsx'
    writer = pd.ExcelWriter(domains_list_path,engine='xlsxwriter')
    data = temp_domains.to_excel(writer, sheet_name = 'Лист 1', index = True)
    writer.save()

    #Save as Excel
    company_list_path = output_path+'company_list.xlsx'
    writer = pd.ExcelWriter(company_list_path,engine='xlsxwriter')
    data = temp_company.to_excel(writer, sheet_name = 'Лист 1', index = True)
    writer.save()
#=================== COMPANY & DOMAINS END ===================

#=================== PREPROCESSING START ===================
url = 'https://www.semrush.com/login/?src=header&redirect_to=%2Fanalytics%2Foverview%2F%3FsearchType%3Ddomain'
path = 'C:/Users/semrush/chromedriver.exe'

#=================== CHOOSE MONTH START ===================
month_list_choose = ['Other number', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

month_list = []
number_list = []
  
number = input('Введите номер месяца, без пробела, через запятую: ')
number_list.append(number)
number_list = [int(x) for xs in number_list for x in xs.split(',')]

number_list = list(set(number_list))
for i in number_list:
    month_list.append(month_list_choose[i])
    
print('Выбранные месяца: ', month_list)
#=================== CHOOSE MONTH END ===================    

#=================== AMOUNT CHOOSING START ===================
def_amount = int(input('Введите кол-во доменов: '))
def_start = int(input('Введите номер начального домена: '))
def_end = def_start + def_amount

print('Номер последенего домена: ', def_end)
#=================== AMOUNT CHOOSING END ===================

#month_list = ['Aug', 'Jul', 'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan']
#month_list = ['Aug', 'Jul']

for x in month_list:
    globals()['traffic_by_countries_list_%s' % x] = []
    
for x in month_list:
    globals()['journey_list_%s' % x] = []

#backlinks_anchors_list = []
#backlinks_refdomains_list = []

visits_list = []
unique_list = []
duration_list = []
bounce_rate_list = []

traffic_sources_list = []
journey_list = []
traffic_by_countries_list = []

#def_amount = 100
#def_start = 526
#def_end = 626
#=================== PREPROCESSING END ===================

#=================== FUNCTION START ===================
df = get_data('www.google.com', def_amount, path, url, def_start, def_end)
#def get_data(first_domain, domain_amount, path, url, start, end)
#=================== FUNCTION END ===================

#=================== DOMAINS START ===================
domains = pd.read_csv('C:/Users/Semrush/domains.csv', sep = ';')
domains['domain'] = domains['domain'].apply(lambda x: ((str(x).replace('https://www.', '')).replace('https://', '')).replace('/', ''))
domains = domains.drop_duplicates()
#=================== DOMAINS END ===================

downloads_path = r"C:/Users/Semrush/Downloads/"
output_path = r"C:/Users/Semrush/Output/"

#=================== OUTPUT START ===================
#backlinks_anchors()
#backlinks_refdomains()
trend_by_devices()
traffic_sources()
journey_sources()
traffic_by_countries(def_amount, month_list)
domains_company(def_start, def_end)
#=================== OUTPUT END ===================
