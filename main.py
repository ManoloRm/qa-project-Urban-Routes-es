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
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        assert test_address_form == data.address_from
        assert test_address_to == data.address_to

    def test_select_comfort(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()

    def test_phone_number(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        WebDriverWait(self.driver, 2)
        self.driver.find_element(By.CLASS_NAME, "np-button").click()
        WebDriverWait(self.driver, 2)
        phone_number = data.phone_number
        assert phone_number == data.phone_number
        phone_text_select = self.driver.find_element(By.ID, 'phone')
        assert (EC.visibility_of_element_located(phone_text_select))
        phone_text_select.send_keys(phone_number)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button').click()
        phone_code = retrieve_phone_code(self.driver)
        phone_code_code_text = self.driver.find_element(By.CSS_SELECTOR, '#code')
        phone_code_code_text.send_keys(phone_code)
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)').click()


    def test_add_new_card(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled').click()
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled').click()
        self.driver.find_element(By.CSS_SELECTOR, '#number').send_keys(data.card_number)
        code_card = self.driver.find_element(By.NAME,'code')
        code_card.send_keys(data.card_code)

    def test_message_driver(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        message_box = self.driver.find_element(By.CSS_SELECTOR, '#comment')
        message_box.send_keys(data.card_number)
        WebDriverWait(self.driver, 20)

    def test_manta_panuelos(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        pages.UrbanRoutesPage.conmfrot_requarments(self)

    def test_helados(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        pages.UrbanRoutesPage.helados_plus(self)
        pages.UrbanRoutesPage.helados_plus(self)

    def test_search_taxi(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        pages.UrbanRoutesPage.search_car(self)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
