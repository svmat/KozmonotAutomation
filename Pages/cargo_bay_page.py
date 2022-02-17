from UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from Pages import left_menu


class CargoBay:
    def __init__(self, browser):
        self.add_new_product_btn = Element(browser, By.XPATH, "//*[text()='Add New Product']")
        self.products_btn = Element(browser, By.XPATH, "//*[text()='Products']")
        self.marketplace_btn = Element(browser, By.XPATH, "//*[text()='Marketplace']")
        self.collection_btn = Element(browser, By.XPATH, "//*[text()='Collection']")
        self.purchases_btn = Element(browser, By.XPATH, "//*[text()='Purchases']")
        self.title_of_page = Element(browser, By.XPATH, "//*[@class='page-title-main']")

    def click_add_new_product_btn(self):
        self.add_new_product_btn.click()

    def click_products_btn(self):
        self.products_btn.click()

    def title_of_page_get_title(self):
        return self.title_of_page.get_text()


