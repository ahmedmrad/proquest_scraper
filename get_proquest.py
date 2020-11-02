import sys
import os
import os.path
import random
import time
import urllib3
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from interaction_webpage import *
from first_dictionary import get_first_dictionary
from rest_dictionary import get_rest_dictionary
from df_generator import create_df
from connect import *


urllib3.disable_warnings()


def main():
    '''
    Get the elements we need and check if we are passing
    the rigth number of arguments
    '''
    if len(sys.argv) != 4:
        (publication, query, start_date, end_date) = sys.argv[1:]
    else:
        print('Please enter four arguments: the publication name, the query, the start date and the end date')
        sys.exit()
    query_formation = '(pub({0}) AND mainsubject({1})) OR (pub({0}) AND ab({1})) OR (pub({0}) AND ti({1}))'.format(
        publication, query)
    print(query_formation)
    path = os.getcwd()
    path_toFiles = '%s\\%s_files' % (path, publication)
    os.makedirs(path_toFiles, exist_ok=True)
    # You might want to check if you need to specify the chromedriver path
    driver = webdriver.Chrome('/put/your/path/chromedriver.exe')
    driver.maximize_window()
    driver.get('https://search.proquest.com/advanced')
    try:
        connect_cbs_secure(driver, query_formation, start_date, end_date)
    except:
        try:
            connect_columbia_network(driver, query_formation, start_date, end_date)
        except:
            connect_other_network(driver, query_formation, start_date, end_date, 'put your uni', 'put your password') # you should add your password and uni
    list_dict = []
    try:
        time.sleep(random.randrange(5, 30))
        navBar_length = get_nav_barNumber(driver)
        while True:
            try:
                if driver.find_element_by_id('endSessionWarningCarryOn').is_displayed() == True:
                    try:
                        time.sleep(random.randrange(5, 30))
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'endSessionWarningCarryOn'))).click()
                        page_start_time = time.time()
                        (num_results, first_range, last_range) = get_ResultsNumber(driver)
                        WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % first_range))).click()
                        time.sleep(random.randrange(5, 30))
                        print('First one done, let us keep pushing', flush=True)
                        list_dict.append(get_first_dictionary(driver))
                        for i in range(2, last_range - first_range + 2):
                            time_now = time.time()
                            WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % (first_range - 1 + i)))).click()
                            time.sleep(random.randrange(5, 30))
                            list_dict.append(get_rest_dictionary(driver, i, first_range))
                            print('Collection_time : %.2f' % (time.time() - time_now))
                            print(i)
                        print('It is done we are moving to the next page.', flush=True)
                        time.sleep(random.randrange(5, 20))
                        print('Time for the page: %.2f' % (time.time() - page_start_time), flush=True)
                        print('#####################################################################', flush=True)
                    except StaleElementReferenceException:
                        time.sleep(random.randrange(5, 30))
                        page_start_time = time.time()
                        (num_results, first_range, last_range) = get_ResultsNumber(driver)
                        WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % first_range))).click()
                        time.sleep(random.randrange(5, 30))
                        print('First one done, let us keep pushing', flush=True)
                        list_dict.append(get_first_dictionary(driver))
                        for i in range(2, last_range - first_range + 2):
                            time_now = time.time()
                            WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % (first_range - 1 + i)))).click()
                            time.sleep(random.randrange(5, 30))
                            list_dict.append(get_rest_dictionary(driver, i, first_range))
                            print('Collection_time : %.2f' % (time.time() - time_now), flush=True)
                            print(i)
                        print('It is done we are moving to the next page.', flush=True)
                        time.sleep(random.randrange(5, 20))
                        print('Time for the page: %.2f' % (time.time() - page_start_time), flush=True)
                        print('#####################################################################', flush=True)
                else:
                    page_start_time = time.time()
                    time.sleep(random.randrange(5, 20))
                    (num_results, first_range, last_range) = get_ResultsNumber(driver)
                    WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % first_range))).click()
                    time.sleep(random.randrange(5, 30))
                    print('First one done, let us keep pushing', flush=True)
                    list_dict.append(get_first_dictionary(driver, first_range))
                    for i in range(2, last_range - first_range + 2):
                        time_now = time.time()
                        WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % (first_range - 1 + i)))).click()
                        time.sleep(random.randrange(5, 30))
                        list_dict.append(get_rest_dictionary(driver, i, first_range))
                        print('Collection_time : %.2f' % (time.time() - time_now), flush=True)
                        print(i)
                    print('It is done we are moving to the next page.', flush=True)
                    time.sleep(random.randrange(5, 20))
                    print('Time for the page: %.2f' % (time.time() - page_start_time), flush=True)
                    print('#####################################################################', flush=True)
                WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContentRight"]/div[4]/div[4]/nav/ul/li[%s]/a' % (navBar_length)))).click()
                time.sleep(random.randrange(5, 30))
            except TimeoutException:
                break
                driver.quit()
    except NoSuchElementException:
        if driver.find_element_by_id('endSessionWarningCarryOn').is_displayed() == True:
            try:
                time.sleep(random.randrange(5, 30))
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'endSessionWarningCarryOn'))).click()
                page_start_time = time.time()
                (num_results, first_range, last_range) = get_ResultsNumber(driver)
                WebDriverWait(driver, random.randrange(5, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % first_range))).click()
                time.sleep(random.randrange(5, 30))
                print('First one done, let us keep pushing', flush=True)
                list_dict.append(get_first_dictionary(driver))
                for i in range(2, last_range - first_range + 2):
                    time_now = time.time()
                    WebDriverWait(driver, random.randrange(5, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % (first_range - 1 + i)))).click()
                    time.sleep(random.randrange(5, 30))
                    list_dict.append(get_rest_dictionary(driver, i, first_range))
                    print('Collection_time : %.2f' % (time.time() - time_now))
                    print(i)
                print('It is done. We only have a page.', flush=True)
                time.sleep(random.randrange(5, 20))
                print('Time for the page: %.2f' % (time.time() - page_start_time), flush=True)
                print('#####################################################################', flush=True)
            except StaleElementReferenceException:
                time.sleep(random.randrange(5, 30))
                page_start_time = time.time()
                (num_results, first_range, last_range) = get_ResultsNumber(driver)
                WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % first_range))).click()
                time.sleep(random.randrange(5, 30))
                print('First one done, let us keep pushing', flush=True)
                list_dict.append(get_first_dictionary(driver))
                for i in range(2, last_range - first_range + 2):
                    time_now = time.time()
                    WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % (first_range - 1 + i)))).click()
                    time.sleep(random.randrange(5, 30))
                    list_dict.append(get_rest_dictionary(driver, i, first_range))
                    print('Collection_time : %.2f' % (time.time() - time_now), flush=True)
                    print(i)
                print('It is done. We only have one page.', flush=True)
                time.sleep(random.randrange(5, 20))
                print('Time for the page: %.2f' % (time.time() - page_start_time), flush=True)
                print('#####################################################################', flush=True)
                driver.quit()
        else:
            page_start_time = time.time()
            time.sleep(random.randrange(5, 20))
            (num_results, first_range, last_range) = get_ResultsNumber(driver)
            WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % first_range))).click()
            time.sleep(random.randrange(5, 30))
            print('First one done, let us keep pushing', flush=True)
            list_dict.append(get_first_dictionary(driver, first_range))
            for i in range(2, last_range - first_range + 2):
                time_now = time.time()
                WebDriverWait(driver, random.randrange(10, 30)).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resultPreviewTrigger_%d"]' % (first_range - 1 + i)))).click()
                time.sleep(random.randrange(5, 30))
                list_dict.append(get_rest_dictionary(driver, i, first_range))
                print('Collection_time : %.2f' % (time.time() - time_now), flush=True)
                print(i)
            print('It is done. We only have one page.', flush=True)
            time.sleep(random.randrange(5, 20))
            print('Time for the page: %.2f' % (time.time() - page_start_time), flush=True)
            print('#####################################################################', flush=True)
            driver.quit()
    create_df(path_toFiles, list_dict, publication, query, start_date, end_date)
    time.sleep(random.randrange(60, 600))


if __name__ == '__main__':
    main()
