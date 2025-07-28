from gc import enable
from operator import truediv

from pygments.lexers import q
from selenium.webdriver.common import by
from selenium.webdriver.support.relative_locator import with_tag_name
from trio import sleep_forever

from helpers import retrieve_phone_code
import data
from selenium import webdriver
import pages
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_set_from_to(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to

    def test_select_confort(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME, 'tcard-title')
        car_comfort = card_title_elements[3]
        assert car_comfort.is_enabled()
        car_comfort.click()
        wait = WebDriverWait(self.driver, 2)


    def test_phone_number(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME,'tcard-title')
        car_comfort = card_title_elements[2]
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 2)
        self.driver.find_element(By.CLASS_NAME, "np-button").click()
        WebDriverWait(self.driver, 2)
        phone_number = data.phone_number
        assert phone_number == data.phone_number
        #phone_text_select = self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > div.np-input > div.input-container' )
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(phone_text_select)).is_enabled()
        #phone_text_select.send_keys(phone_number)
        TELEPHONE_NUMBER_FIELD = self.driver.find_element (By.CLASS_NAME, 'np-text')
        TELEPHONE_NUMBER_FIELD.send_keys(phone_number)
        WebDriverWait(self.driver, 2)
        phone_code = retrieve_phone_code(driver=self.driver)
        phone_code_code_text = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.np-input > div')
        phone_code_code_text.send_keys(phone_number)
        assert phone_code == retrieve_phone_code(driver=self.driver)
        WebDriverWait(self.driver, 2)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.np-input > div').send_keys(phone_code)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button').click()

        @classmethod
    def teardown_class(cls):
        cls.driver.quit()
