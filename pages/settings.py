from selenium.webdriver.common.by import By

from fixtures.models.settings_model import SettingsData
from pages.base_page import BasePage


class Settings(BasePage):
    def add_settings(self, data:SettingsData):
        self.fill_element(data=data.name, locator=(By.ID, 'id_firstname'))
        self.fill_element(data=data.email, locator=(By.ID, 'id_email'))
        self.fill_element(data=data.lastname, locator=(By.ID, 'id_lastname'))
        self.fill_element(data=data.city, locator=(By.ID, 'id_city'))
        self.click_element(locator=(By.ID, 'id_submitbutton'))