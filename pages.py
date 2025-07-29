from selenium import webdriver
import data
import helpers
from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    to_field = (By.ID, 'to')
    button_round = (By.ID, 'button round')
    payment_button = (By.ID, "pp-button filled")
    phon_num = (By.CLASS_NAME, 'np-button')
    car_comfort = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div.tcard.active > button')


    def __init__(self, driver):
        self.driver = driver

    def get_button_round(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()

    #def get_payment_button(self):

    def set_from(self, from_address):
        self.driver.find_element(By.ID, 'from').send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(By.ID, 'to').send_keys(to_address)

    def get_from(self):
        return self.driver.find_elemen(By.ID, 'from').get_property('value')

    def get_to(self):
        return self.driver.find_element(By.ID, 'to').get_property('value')

    def select_rout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.modes-container > div.mode.active').click()

    def set_phone(self):
        self.driver.find_element(*self.button_round).click()
        self.driver.send_keys(data.phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.button_round).get_property('value')

    def set_card_number(self):
        self.driver.find_element(*self.button_round).click()

    def get_confort(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button')

    def get_confort_nt(self):
        return  self.driver.find_elements(By.CLASS_NAME, 'tcard-title')

    def set_confort(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div.tcard.active > button')

