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
        pages.UrbanRoutesPage.phone_text(self)
        phone_number = data.phone_number
        assert phone_number == data.phone_number
        phone_text_select = self.driver.find_element(By.ID, 'phone')
        assert (EC.visibility_of_element_located(phone_text_select))
        phone_text_select.send_keys(phone_number)
        pages  .UrbanRoutesPage.phone_button_next(self)
        phone_code = retrieve_phone_code(self.driver)
        phone_code_code_text = self.driver.find_element(By.CSS_SELECTOR, '#code')
        phone_code_code_text.send_keys(phone_code)
        pages.UrbanRoutesPage.set_phone_confirm_code(self)


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
        pages.UrbanRoutesPage.add_card_buttons(self)
        pages.UrbanRoutesPage.card_code(self)

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


    def test_blanket_scarves(self):
        self.driver.get(data.urban_routes_url)
        test_address_form = data.address_from
        test_address_to = data.address_to
        pages.UrbanRoutesPage.set_from(self, test_address_form)
        pages.UrbanRoutesPage.set_to(self, test_address_to)
        pages.UrbanRoutesPage.get_button_round(self)
        car_comfort = pages.UrbanRoutesPage.set_confort(self)
        assert car_comfort.is_enabled()
        car_comfort.click()
        pages.UrbanRoutesPage.get_scarve_blanket(self)


    def test_icecream(self):
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
