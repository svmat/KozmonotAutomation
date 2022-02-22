from UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class LeftMenu:
    def __init__(self, browser):
        self.logo_sign = Element(browser, By.XPATH, "//*[@src='/static/media/logo-dark.6e02fbea.png']")
        self.dashboard_btn = Element(browser, By.XPATH, "//*[text()='Dashboard']")
        self.console_btn = Element(browser, By.XPATH, "//*[text()='Console']")
        self.cargo_bay_btn = Element(browser, By.XPATH, "//*[text()='Cargo Bay']")

    def click_dashboard_btn(self):
        self.dashboard_btn.click()

    def click_console_btn(self):
        self.console_btn_btn.click()

    def click_cargo_bay_btn(self):
        self.cargo_bay_btn.click()
