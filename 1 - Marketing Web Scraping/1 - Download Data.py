#!/usr/bin/env python
# coding: utf-8

#=================== LIBRARIES ===================
from selenium.webdriver.common.action_chains import ActionChains # Step-by-step
from selenium.webdriver.support import expected_conditions # Check input authorization
from selenium.webdriver.support.ui import WebDriverWait # Check if the authorization in the output is true (by choice)
from dateutil.relativedelta import relativedelta # Timedelta
from selenium.webdriver.common.keys import Keys # Keys given
from selenium.webdriver.common.by import By # Select XPATH
from selenium import webdriver # Select WebDriver (chrome)
import pandas as pd
import datetime
import random 
import time
import glob
import os

# Def function to scroll down
class scroll:
    def __init__(start_num, step, end_num, scroll):
        self.start_num = start_num
        self.step = step
        self.end_num = end_num
        self.scroll = scroll
        
    def random_num(start_num, end_num):
        random_number = random.randrange(start_num,
                                         end_num, 
                                         random.randrange(50, 100, 
                                                          random.randrange(10, 25, 4)))
        return random_number
    
    def scroll_down(self):
        num_1 = self.start_num
        
        if self.scroll == 'short':
            for i in range(0, 2):
            driver.execute_script("window.scrollTo("+ str(num_1) +","+ \
                                  str(self.random_num(num_1 + self.step)) +");")
            num_1 += self.step_1
            time.sleep(random.randrange(2, 4, 1))
            
        if self.scroll == 'long':
            for i in range(0, 7):
            driver.execute_script("window.scrollTo("+ str(num_1) +","+ \
                                  str(self.random_num(num_1 + self.step)) +");")
            num_1 += self.step_1
            time.sleep(random.randrange(2, 4, 1))
            
        driver.execute_script("window.scrollTo("+ str(num_1) +","+ \
                              str(self.end_num) +");")
        
    def scroll_up(self):
        num_1 = self.start_num
        
        if self.scroll == 'short':
            for i in range(0, 2):
            driver.execute_script("window.scrollTo("+ str(num_1) +","+ \
                                  str(self.random_num(num_1 - self.step)) +");")
            num_1 += self.step_1
            time.sleep(random.randrange(2, 4, 1))
            
        if self.scroll == 'long':
            for i in range(0, 7):
            driver.execute_script("window.scrollTo("+ str(num_1) +","+ \
                                  str(self.random_num(num_1 - self.step)) +");")
            num_1 += self.step_1
            time.sleep(random.randrange(2, 4, 1))
            
        driver.execute_script("window.scrollTo("+ str(num_1) +","+ \
                              str(self.end_num) +");")
        
class downloader_prepare:
# ===== INIT
    def __init__(self, login, password, demo_domain, driver_path, url, download_path):
        self.login = login
        self.password = password
        self.demo_domain = demo_domain
        self.driver_path = driver_path
        self.url = url
        self.download_path = download_path

# ===== LOG IN
    def log_in(self):
        # Browser profile display options
        options = webdriver.ChromeOptions()

        # Choose download path
        prefs = {"download.default_directory":r"{}".format(self.download_path),
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True}

        options.add_experimental_option('prefs', prefs)

        # Hide WebDriver usage    
        options.add_argument("--disable-blink-features=AutomationControlled")

        # WebDriver path
        driver = webdriver.Chrome(executable_path = self.driver_path, options = options)

        # Set browser window size
        driver.set_window_size(1600,1600)

        # WebDriver start
        driver.get(self.url)

        # Enter login information
        log_in_successfully = False
        while not log_in_successfully:
            try:
                try:
                    time.sleep(random.randrange(2, 5, 1))
                    email = WebDriverWait(driver, 
                                         random.randrange(2, 5, 1)
                                         ).until(
                                        expected_conditions.presence_of_element_located((By.ID, "email")))
                    email.send_keys(f'{self.login}')
                    WebDriverWait(driver,
                                 random.randrange(2, 5, 1)
                                 ).until(lambda browser: email.get_attribute('value') == f'{self.login}')
                    print("Login input: Succeed")
                except:
                    print("Login input: Failed")

                try:
                    time.sleep(random.randrange(2, 5, 1))
                    password = WebDriverWait(driver, 
                                            random.randrange(2, 5, 1)
                                            ).until(
                            expected_conditions.presence_of_element_located((By.ID, "password")))
                    password.send_keys(f'{self.password}')
                    WebDriverWait(driver, 
                                 random.randrange(2, 5, 1)
                                 ).until(lambda browser: password.get_attribute('value') == f'{self.password}')
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
            
    
# ===== DEMO DOMAIN
    def demo_domain(self):
        # Enter domain
        time.sleep(random.randrange(4, 8, 1))
        search = driver.find_element(By.XPATH,
                                     '//*[@class="___SValue_12tss-red-team _size_l_12tss-red-team"]')
        search.send_keys(self.demo_domain)
        WebDriverWait(driver, 
                      random.randrange(4, 8, 1)
                     ).until(lambda browser: search.get_attribute('value') == self.demo_domain)
        search.submit()
        time.sleep(random.randrange(10, 15, 1))
        print('Demo domain sended')    
    
class downloader_main:
    def __init__(self, domain_file, start, end,
                 overview = False,
                 backlinks = False,
                 anchors = False,
                 tbd_visits = False,
                 tbd_unique = False,
                 tbd_duration = False,
                 tbd_bounce_rate = False,
                 traffic_sources = False,
                 traffic_journey = False,
                 traffic_countries = False
                 status_alert = False
                ):
        self.domain_file = domain_file # Full path to domain file (csv)
        self.domain_amount = end - start # Domain number
        self.start = start # First domain
        self.end = end # Last domain
        
        self.overview = overview # OVERVIEW
        self.backlinks = backlinks # BACKLINKS 
        self.anchors = anchors # ANCHORS 
        self.tbd_visits = tbd_visits #TREND BY DEVICE !VISITS! 
        self.tbd_unique = tbd_unique #TREND BY DEVICE !UNIQUE! 
        self.tbd_duration = tbd_duration #TREND BY DEVICE !DURATION! 
        self.tbd_bounce_rate = tbd_bounce_rate #TREND BY DEVICE !BOUNCE RATE! 
        self.traffic_sources = traffic_sources #TRAFFIC SOURCES 
        self.traffic_journey = traffic_journey #TRAFFIC JOURNEY 
        self.traffic_countries = traffic_countries #TRAFFIC COUNTRIES
        
        self.status_alert = status_alert
    
    def main_loop(self):
        # List of executed domains
        domain_list = []
        # Start while loop
        while len(domain_list) < domain_amount:
            time.sleep(random.randrange(2, 5, 1))

            if not (len(domain_list) >= domain_amount):
                
                domain_path = r'{}'.format(self.domain_file)
                domain_path = domain_path.reaplace(('\\', '/') + '/'
                                                   
                domains = pd.read_csv(f'{domain_path}domain.csv', sep = ';')['domain']
                domains = domains.apply(lambda x: ((str(x).replace('https://www.', '')) \
                                                   .replace('https://', '')).replace('/', ''))
                domains = domains.drop_duplicates()

                for domain in domains.iloc[start:end]:

                    print((int(end) - len(domain_list)), 'domains left')

                    print("START:",domain)

#================== SEARCHBAR
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
                                # Enter domain
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

                    #print("Work on the domain",domain,"has started")
                    time.sleep(random.randrange(2, 5, 1))

#------------------ DOMAIN OVERVIEW

#================== OVERVIEW TREND (overview-trend.xlsx)
                    if self.overview == True:
                        overview_trend = False
                        try_again = 3

                        while not (try_again == 0):
                            try:

                                #Button Export
                                export = driver.find_element(By.XPATH, '//*[@class="___SBody_cju2a-red-team"]//*[@class="___SButton_1gip4-red-team _size_m_1gip4-red-team _theme_secondary-muted_1gip4-red-team"]').click()
                                time.sleep(random.randrange(2, 5, 1))

                                #Select CSV(semilcolon)
                                csv = driver.find_element(By.XPATH, '//*[@class="___SContainer_6papi-red-team"]//div//*[@value="stdcsv"]').click()
                                time.sleep(random.randrange(2, 5, 1))

                                print("--- Overview Trend export: Succeed")
                                try_again = 0
                                overview_trend = True

                            except:
                                try_again = try_again - 1
                                print("!!! Overview Trend export: Failed. Tries left:", try_again)
                        #print("Overview Trend export status:",overview_trend)


#---------------------- Scroll down
                        scroll(0, 400, 3200, 'long').scroll_down()
                        
#================== BACKLINKS (backlinks_refdomains.xlsx)
                    
                    <CODE HERE>    
                    
#================== ANCHORS (backlinks_anchors.xlsx)
                                                   
                    <CODE HERE>    

#================== Navigation
                    export = driver.find_element(By.XPATH, '//*[@id="srf-sidebar"]//div[contains(@class,"srf-report-sidebar-main__group js-sidebar-group")]//div[contains(@id,"accordion-content-seo")]//a[contains(@data-test,"seo_traffic_analytics")]').click()
                    time.sleep(random.randrange(5, 8, 1))
                    print("Change page: Traffic Analytics")

#------------------ TRAFFIC ANALYTICS

#================== TREND BY DEVICE !VISITS!(Trend By Devices.xlsx)
                    if self.tbd_visits == True:
                        visits = False
                        try_again = 3

                        while not (try_again == 0):
                            try:

                                #Button Export
                                export = driver.find_element(By.XPATH, '//*[@id="chartOverviewVisitsHistory"]//*[@class="___SBoxInline_8om4t_gg_ ___SButton_1gip4_gg_ _size_m_1gip4_gg_ _size_m_wus9c_gg_ _theme_secondary-muted_1gip4_gg_"]').click()
                                #time.sleep(random.randrange(2, 5, 1))
                                time.sleep(random.randrange(1, 4, 1))

                                #Select CSV
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

#================== TREND BY DEVICE !UNIQUE! (Trend By Devices.xlsx)
                                                   
                    <CODE HERE>    

#================== TREND BY DEVICE !DURATION! (Trend By Devices.xlsx)
                                                   
                    <CODE HERE>    

#================== TREND BY DEVICE !BOUNCE RATE! (Trend By Devices.xlsx)
                                                   
                    <CODE HERE>                       

#================== TRAFFIC SOURCES (Traffic Sources by Type.xlsx)
                                                   
                    <CODE HERE>    

#------------------ TRAFFIC JOURNEY

#================== TRAFFIC JOURNEY  (All sources.xlsx)
                    if self.traffic_journey == True:
                        for x in month_list:


                            traffic_by_countries_2 = False
                            try_again = 3

                            while not (try_again == 0):
                                try:

                                    #Button 
                                    export = driver.find_element(By.XPATH, '//a[@data-ui-name="MonthRangePicker.Trigger"]').click()
                                    time.sleep(random.randrange(1, 4, 1))

                                    #Button 
                                    export = driver.find_element(By.XPATH, '//button[@aria-label="'+x+' 1, 2022"]').click()
                                    time.sleep(random.randrange(1, 4, 1))

                                    #Button 
                                    export = driver.find_element(By.XPATH, '//div[@data-ui-name="Dropdown.Popper"]//button[@data-test="selector-apply"]').click()
                                    time.sleep(random.randrange(1, 4, 1))

                                    #---------------Scroll down
                                    scroll(0, 250, 900, 'short').scroll_down()
                                    
                                    #---------------TRAFFIC JOURNEY (All Sources.xlsx)
                                    journey = False
                                    try_again = 3

                                    while not (try_again == 0):
                                        try:

                                            #Button CSV
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

                                    #---------------Scroll up
                                    scroll(900, 350, 0, 'short').scroll_up()

                                    print("--- Month "+x+" changed: Succeed")
                                    journey_list.append(domain)
                                    try_again = 0
                                    traffic_by_countries_2 = True

                                except:
                                    try_again = try_again - 1
                                    print("!!! Month changed: Failed. Tries left:", try_again)
                        #print("traffic_by_countries_2 status:",traffic_by_countries_2)

#================== Navigation
                    export = driver.find_element(By.XPATH, '//*[@class="sc-1bc4zew-0 ccJnmu"]//div[contains(@class,"___STabLine_nxhjn_gg_ __underlined_nxhjn_gg_ _size_m_nxhjn_gg_")]//button[contains(@data-test,"reportTab geo")]').click()
                    time.sleep(random.randrange(5, 8, 1))
                    print("Change menu link: Traffic Analytics:Geo Distribution")

#------------------ TRAFFIC GEO DISTRIBUTION

#================== TRAFFIC COUNTRIES  (Traffic by Country.xlsx)
                                                   
                    <CODE HERE>    

#================== STATUS ALERT
                    if self.status_alert == True:
                        # Alerts on the end of downloading files for a domain
                        print("END:",domain)
                        time.sleep(random.randrange(1, 4, 1))

                    # Add the completed domain to the list
                    domain_list.append(domain)
                    #print("Domain",domain,"added in domain_list.")

