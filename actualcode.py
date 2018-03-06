from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class WebAutomata(object):

    def __init__(self, url):
    	self.options = Options()
    	self.options.add_argument('-headless')
        self.driver = webdriver.Firefox(firefox_options=self.options)
        self.url = url
        self.driver.get(url)

    def interactPPS(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '//input[@data-test="universal-search-text-box"]'))).send_keys('Fever')
        self.driver.implicitly_wait(2)
        sections = []
        self.driver.find_element(By.XPATH, '//div[@data-test="pps-results"]')
        for option, section in enumerate(self.driver.find_elements(By.XPATH, '/html/body/div/main/div[1]/section/form/div[1]/div[2]/div[3]/div[1]/div')):
            print option, section.text
            sections.append(section.text)
        self.driver.get_screenshot_as_file('PPS Search.png')
        return sections

    def closedriver(self):
        self.driver.close()

