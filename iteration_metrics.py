import random
import time
from selenium.common.exceptions import StaleElementReferenceException


def get_ResultsNumber(driver):
    '''
    Method to get several iteration metrics
    :param driver: selenium chrome driver
    :return num_results: int, number of results per page
    :return first_range: int, first page result index as it appears on scraped page
    :return last_range: int, last page result index as it appears on scraped page
    '''
    try:
        time.sleep(random.randrange(5, 30))
        pagination = driver.find_element_by_xpath('//*[@id="mainContentRight"]/div[2]/div/div[1]/label').text
        pages = list(map(int, (pagination.split()[1]).split('-')))
        first_range = pages[0]
        last_range = pages[1]
        num_results = pages[1] - pages[0] + 1
    except StaleElementReferenceException:
        time.sleep(random.randrange(5, 30))
        pagination = driver.find_element_by_xpath('//*[@id="mainContentRight"]/div[2]/div/div[1]/label').text
        pages = list(map(int, (pagination.split()[1]).split('-')))
        first_range = pages[0]
        last_range = pages[1]
        num_results = pages[1] - pages[0] + 1
    return num_results, first_range, last_range


def get_nav_barNumber(driver):
    '''
    Method to get the length of the navigation
    bar in order to correctly click on
    the next button to move around the website
    :param driver: selenium chrome driver
    :return nav_bar_length: str
    '''
    nav_bar = driver.find_element_by_class_name('pagination').text
    nav_test = ' '.join(nav_bar.split("\n"))
    nav_list = nav_test.split()
    first_el = nav_list[0]
    second_el = '_'.join(nav_list[1:3])
    rest = nav_list[3:-2]
    last_el = '_'.join(nav_list[-2:])
    rest.insert(0, second_el)
    rest.insert(0, first_el)
    rest.insert(len(rest), last_el)
    nav_bar_length = str(len(rest))
    return nav_bar_length
