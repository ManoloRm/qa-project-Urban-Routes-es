from selenium import webdriver
import data
import helpers
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_round = (By.ID, 'button round')
    payment_button = (By.ID, "pp-button filled")
    confort_button = (By.ID)
    phonh_num = (By.CLASS_NAME, 'np-button')


    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def select_rout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.modes-container > div.mode.active').click()

    def set_phone(self):
        self.driver.find_element(*self.button_round).click()
        self.driver.send_keys(data.phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.button_round).get_property('value')

    def set_card_number(self):
        self.driver.find_element(*self.button_round).click()
