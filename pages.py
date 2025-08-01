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
    blanket_scarves = (By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body ' '> div:nth-child(1) > div > div.r-sw > div > span')

    def __init__(self, driver):
        self.driver = driver

    def get_button_round(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button').click()

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

    def set_phone_confirm_code(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)').click()

    def phone_text(self):
        self.driver.find_element(By.ID, 'phone').send_keys(data.phone_number)

    def get_phone(self):
        return self.driver.find_element(*self.button_round).get_property('value')

    def phone_message(self):
        self.driver.find_element(By.CSS_SELECTOR, '#comment').sendkeys(data.message_for_driver)

    def set_card_number(self):
        self.driver.find_element(*self.button_round).click()

    def get_confort(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown > div.results-container > div.results-text > button')

    def get_confort_note(self):
        return  self.driver.find_elements(By.CLASS_NAME, 'tcard-title')

    def set_confort(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.tariff-cards > div:nth-child(5)')

    def get_confirm_phone(self):
        return self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button').click()

    def confirm_phone_code(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button:nth-child(1)').click()

    def conmfrot_requarments(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body ' '> div:nth-child(1) > div > div.r-sw > div > span').click()

    def helados_plus(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                           '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body '
                                           '> div.r.r-type-group > div > div.r-group-items > div:nth-child(1) > div > div.r-counter > div > div.counter-plus').click()
    def search_car(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.smart-button-wrapper').click()

    def phone_button_next(self):
        self.driver.find_element(By.CSS_SELECTOR,
                                 '#root > div > div.number-picker.open > div.modal > div.section.active > form > div.buttons > button').click()
    def phone_text(self):
        self.driver.find_element(By.CLASS_NAME, "np-button").click()

    def add_card_buttons(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.pp-button.filled').click()
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.payment-picker.open > div.modal > div.section.active > div.pp-selector > div.pp-row.disabled').click()
        self.driver.find_element(By.CSS_SELECTOR, '#number').send_keys(data.card_number)

    def card_code(self):
        self.driver.find_element(By.NAME, 'code').send_keys(data.card_code)

    def get_scarve_blanket(self):
        self.driver.find_element(By.CSS_SELECTOR, '#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.reqs.open > div.reqs-body ' '> div:nth-child(1) > div > div.r-sw > div > span').click()
