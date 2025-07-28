import re
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
        car_comfort = card_title_elements[4]
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
        car_comfort = card_title_elements[4]
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 2)
        self.driver.find_element(By.CLASS_NAME, "np-button").click()
        WebDriverWait(self.driver, 2)
        phone_number = data.phone_number
        assert phone_number == data.phone_number
        phone_text_select = self.driver.find_element(By.CSS_SELECTOR,'#root > div > div.number-picker.open > div.modal > div.section.active > form > div.np-input > div.input-container')
        assert (EC.visibility_of_element_located(phone_text_select))
        phone_text_select.send_keys(phone_number)
        WebDriverWait(self.driver, 2)
        phone_code = retrieve_phone_code(driver=self.driver)
        phone_code_code_text = self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.np-input > div')
        phone_code_code_text.send_keys(phone_number)
        assert phone_code == retrieve_phone_code(driver=self.driver)
        WebDriverWait(self.driver, 2)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.np-input > div').send_keys(phone_code)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)').click()
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button').click()

    def test_add_new_card(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME,'tcard-title')
        car_comfort = card_title_elements[4]
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 20)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled').click()
        WebDriverWait(self.driver, 100)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled').click()
        WebDriverWait(self.driver, 20)
        self.driver.find_element(By.CSS_SELECTOR, '#number').send_keys(data.card_number)
        WebDriverWait(self.driver, 20)
        code_card_elements = self.driver.find_elements(By.CLASS_NAME,'code')
        code_card = code_card_elements[3]
        WebDriverWait(self.driver, 20)
        code_card.send_keys(data.card_code)

    def test_message_driver(self):
        self.driver.get(data.urban_routes_url)
        message_test = data.message_for_driver
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME, 'tcard-title')
        car_comfort = card_title_elements[4]
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 20)
        message_box = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div')
        message_box.click()
        message_box.send_keys(message_test)
        WebDriverWait(self.driver, 20)

    def test_manta_panuelos(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME, 'tcard-title')
        car_comfort = card_title_elements[4]
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 20)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body '
                                                  '> div:nth-child(1) > div > div.r-sw > div > span').click()

    def test_helados(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME, 'tcard-title')
        car_comfort = card_title_elements[4]
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 20)
        helado_count = self.driver.find_element(By.CSS_SELECTOR,
                                                '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body '
                                                '> div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-value')
        helados = self.driver.find_element(By.CSS_SELECTOR,
                                           '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body '
                                           '> div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus')
        helados.click()
        helados.click()

    def test_search_taxi(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        self.driver.find_element(By.XPATH, '//*[@id="from"]').send_keys(test_address_form)
        self.driver.find_element(By.XPATH, '//*[@id="to"]').send_keys(test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()
        card_title_elements = self.driver.find_elements(By.CLASS_NAME, 'tcard-title')
        car_comfort = card_title_elements[4]
        assert car_comfort.is_enabled()
        car_comfort.click()
        #EC.visibility_of_element_located(By.)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper').click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
