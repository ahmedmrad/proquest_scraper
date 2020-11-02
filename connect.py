from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


def connect_other_network(driver, query_formation, start_date, end_date, username, password):
    '''
    method to connect to proquest through any other network
    :param driver: selenium chrome driver
    :param query_formation: search query
    :param start_date: start date of the query
    :param end_date: end date of the query
    :param username: network username
    :param password: network password
    '''
    school_find = driver.find_element_by_id('institutionName')
    school_find.send_keys('columbia university')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'findInstitution'))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="institution-layer"]/div[1]/span[2]/a'))).click()
    username = driver.find_element_by_xpath('//*[@id="username"]')
    password = driver.find_element_by_xpath('//*[@id="password"]')
    username.send_keys(username)
    password.send_keys(password)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="fm1"]/div[3]/input[4]'))).click()
    element = driver.find_element_by_id('queryTermField')
    element.send_keys(query_formation)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchToResultPage'))).click()
    Result_Per_Page = Select(driver.find_element_by_id('itemsPerPage'))
    Result_Per_Page.select_by_value('100')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'customDateRangeLink'))).click()
    startingDate = driver.find_element_by_id('startingDate')
    endingDate = driver.find_element_by_id('endingDate')
    startingDate.send_keys(start_date)
    endingDate.send_keys(end_date)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'dateRangeSubmit'))).click()


def connect_columbia_network(driver, query_formation, start_date, end_date):
    '''
    connect to proquest through a columbia non secure network
    :param driver: selenium chrome driver
    :param query_formation: search query
    :param start_date: start date of the query
    :param end_date: end date of the query
    '''
    select = Select(driver.find_element_by_id('accounts'))
    select.select_by_value('10226')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'useAccount'))).click()
    element = driver.find_element_by_id('queryTermField')
    element.send_keys(query_formation)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchToResultPage'))).click()
    Result_Per_Page = Select(driver.find_element_by_id('itemsPerPage'))
    Result_Per_Page.select_by_value('100')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'customDateRangeLink'))).click()
    startingDate = driver.find_element_by_id('startingDate')
    endingDate = driver.find_element_by_id('endingDate')
    startingDate.send_keys(start_date)
    endingDate.send_keys(end_date)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'dateRangeSubmit'))).click()


def connect_cbs_secure(driver, query_formation, start_date, end_date):
    '''
    connect to proquest through a columbia secure network
    :param driver: selenium chrome driver
    :param query_formation: search query
    :param start_date: start date of the query
    :param end_date: end date of the query
    '''
    element = driver.find_element_by_id('queryTermField')
    element.send_keys(query_formation)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'searchToResultPage'))).click()
    Result_Per_Page = Select(driver.find_element_by_id('itemsPerPage'))
    Result_Per_Page.select_by_value('100')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'customDateRangeLink'))).click()
    startingDate = driver.find_element_by_id('startingDate')
    endingDate = driver.find_element_by_id('endingDate')
    startingDate.send_keys(start_date)
    endingDate.send_keys(end_date)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'dateRangeSubmit'))).click()
