import random
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def get_rest_dictionary(driver, i, first_range):
    '''
    method to create the dictionnary out of the collected data after the first element:
    :param driver: selenium chrome driver
    :param i: proquest page iterator
    :param first_range: second iterator specific to the structure of proquest
    :return dictionnary: dictionnary
    '''
    index_name = []
    index_data = []
    list_element = ['title', 'author', 'publication',
                    'abstract_summary', 'subejct_terms']
    if driver.find_element_by_id('endSessionWarningCarryOn').is_displayed() == True:
        try:
            time.sleep(random.randrange(5, 30))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
                (By.ID, 'endSessionWarningCarryOn'))).click()
            for element in list_element:
                if element == 'title':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_id(
                            'result-header-%d' % (first_range + i - 1)).text)
                        print(driver.find_element_by_id('result-header-%d' %
                                                        (first_range + i - 1)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'author':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % (first_range + i - 1)).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % (first_range + i - 1)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'publication':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % (first_range + i - 1)).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % (first_range + i - 1)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'abstract_summary':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/p[2]' % (i - 2)).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/p[2]' % (i - 2)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'subejct_terms':
                    try:
                        index_name.append(element)
                        index_data.append((driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/div[2]/div[2]/div[2]' % (i - 2)).text).replace('\n', ' ').replace(';', ' #'))
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/div[2]/div[2]/div[2]' % (i - 2)).text, flush=True)
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
                            'result-header-%d' % (first_range + i - 1)).text)
                        print(driver.find_element_by_id('result-header-%d' %
                                                        (first_range + i - 1)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'author':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % (first_range + i - 1)).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % (first_range + i - 1)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'publication':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % (first_range + i - 1)).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % (first_range + i - 1)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'abstract_summary':
                    try:
                        index_name.append(element)
                        index_data.append(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/p[2]' % (i - 2)).text)
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/p[2]' % (i - 2)).text, flush=True)
                    except NoSuchElementException:
                        pass
                elif element == 'subejct_terms':
                    try:
                        index_name.append(element)
                        index_data.append((driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/div[2]/div[2]/div[2]' % (i - 2)).text).replace('\n', ' ').replace(';', ' #'))
                        print(driver.find_element_by_xpath(
                            '//*[@id="resultPreviewLayerZone_%d"]/div/div[2]/div[2]/div[2]' % (i - 2)).text, flush=True)
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
                        'result-header-%d' % (first_range + i - 1)).text)
                    print(driver.find_element_by_id('result-header-%d' %
                                                    (first_range + i - 1)).text, flush=True)
                except NoSuchElementException:
                    pass
            elif element == 'author':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % (first_range + i - 1)).text)
                    print(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[1]' % (first_range + i - 1)).text, flush=True)
                except NoSuchElementException:
                    pass
            elif element == 'publication':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % (first_range + i - 1)).text)
                    print(driver.find_element_by_xpath(
                        '//*[@id="mldcopy%d"]/div[1]/div[2]/span[2]' % (first_range + i - 1)).text, flush=True)
                except NoSuchElementException:
                    pass
            elif element == 'abstract_summary':
                try:
                    index_name.append(element)
                    index_data.append(driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone_%d"]/div/p[2]' % (i - 2)).text)
                    print(driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone_%d"]/div/p[2]' % (i - 2)).text, flush=True)
                except NoSuchElementException:
                    pass

            elif element == 'subejct_terms':
                try:
                    index_name.append(element)
                    index_data.append((driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone_%d"]/div/div[2]/div[2]/div[2]' % (i - 2)).text).replace('\n', ' ').replace(';', ' #'))
                    print(driver.find_element_by_xpath(
                        '//*[@id="resultPreviewLayerZone_%d"]/div/div[2]/div[2]/div[2]' % (i - 2)).text, flush=True)
                except NoSuchElementException:
                    pass
            else:
                pass
    dictionary = dict(zip(index_name, index_data))
    return dictionary
