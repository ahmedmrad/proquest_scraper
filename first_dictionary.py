import random
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def get_first_dictionary(driver, first_range):
    '''
    Method to create the dictionnary out of the collected data for the first element
    :param driver: selenium chrome driver
    :param first_range: first page
    :return dictionnary:  dictionnary, containing 'title', 'author', 'publication','abstract_summary', 'subejct_terms'
    '''
    index_name = []
    index_data = []
    list_element = ['title', 'author', 'publication',
                    'abstract_summary', 'subejct_terms']
    if driver.find_element_by_id('endSessionWarningCarryOn').is_displayed() == True:
        try:
            time.sleep(random.randrange(5, 30))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'endSessionWarningCarryOn'))).click()
            for element in list_element:
                if element == 'title':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_id(
                            'result-header-%d' % first_range).text)
                        print(driver.find_element_by_id(
                            'result-header-%d' % first_range).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'author':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % first_range).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % first_range).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'publication':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % first_range).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % first_range).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'abstract_summary':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/p[2]').text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/p[2]').text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'subejct_terms':
                    try:
                        index_name.append(element)
                        index_data.append((driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/div[2]/div[2]/div[2]').text).replace('\n', ' ').replace(';', ' #'))
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/div[2]/div[2]/div[2]').text, flush=True)
                    except NoSuchElementException:
                        pass
                else:
                    pass
        except StaleElementReferenceException:
            time.sleep(random.randrange(5, 30))
            for element in list_element:
                if element == 'title':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_id(
                            'result-header-%d' % first_range).text)
                        print(driver.find_element_by_id(
                            'result-header-%d' % first_range).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'author':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % first_range).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % first_range).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'publication':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % first_range).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % first_range).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'abstract_summary':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/p[2]').text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/p[2]').text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'subejct_terms':
                    try:
                        index_name.append(element)
                        index_data.append((driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/div[2]/div[2]/div[2]').text).replace('\n', ' ').replace(';', ' #'))
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone"]/div/div[2]/div[2]/div[2]').text, flush=True)
                    except NoSuchElementException:
                        pass
                else:
                    pass
    else:
        for element in list_element:
            if element == 'title':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_id(
                        'result-header-%d' % first_range).text)
                    print(driver.find_element_by_id(
                        'result-header-%d' % first_range).text)
                except NoSuchElementException:
                    pass
            elif element == 'author':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % first_range).text)
                    print(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % first_range).text, flush=True)
                except NoSuchElementException:
                    pass
            elif element == 'publication':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % first_range).text)
                    print(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % first_range).text, flush=True)
                except NoSuchElementException:
                    pass
            elif element == 'abstract_summary':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone"]/div/p[2]').text)
                    print(driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone"]/div/p[2]').text, flush=True)
                except NoSuchElementException:
                    pass

            elif element == 'subejct_terms':
                try:
                    index_name.append(element)
                    index_data.append((driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone"]/div/div[2]/div[2]/div[2]').text).replace('\n', ' ').replace(';', ' #'))
                    print(driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone"]/div/div[2]/div[2]/div[2]').text, flush=True)
                except NoSuchElementException:
                    pass
            else:
                pass
    dictionary = dict(zip(index_name, index_data))
    return dictionary
