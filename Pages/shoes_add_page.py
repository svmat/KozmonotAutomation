from UIElement import UIElement as Element
from selenium.webdriver.common.by import By



class ShoesAdd:
    def __init__(self, browser):
        # required fields
        self.name = Element(browser, By.XPATH, "//*[@name='shoeName']")
        self.format = Element(browser, By.XPATH, "//*[@name='productFormat']")
        self.format_option = Element(browser, By.XPATH, "//*[@value='Sneaker']")
        self.cond = Element(browser, By.XPATH, "//*[@name='condition']")
        self.cond_option = Element(browser, By.XPATH, "//select[@name='condition']/option[@value='Brand New']")
        self.opening_price = Element(browser, By.XPATH, "//*[@name='openingPrice']")
        self.size = Element(browser, By.XPATH, "//*[@name='size']")
        self.size_option = Element(browser, By.XPATH, "//*[@value='1']")
        self.quantity = Element(browser, By.XPATH, "//*[@name='quantity']")
        self.box_condition = Element(browser, By.XPATH, "//*[@name='boxCondition']")
        self.box_condition_option = Element(browser, By.XPATH, "//div[1]/div[3]/div[2]/select/option[3]")
        self.asking_price = Element(browser, By.XPATH, "//*[@name='askingPrice']")

        # non required fiefls
        self.release_year = Element(browser, By.XPATH, "//*[@name='releaseYear']")
        self.release_year_option = Element(browser, By.XPATH, "//*[@value='2022']")
        self.country = Element(browser, By.XPATH, "//*[@name='country']")
        self.country_option = Element(browser, By.XPATH, "//*[@value='Afghanistan']")
        self.brand = Element(browser, By.XPATH, "//*[@name='brand']")
        self.colorway = Element(browser, By.XPATH, "//*[@name='colorway']")
        self.features = Element(browser, By.XPATH, "//*[@name='features']")
        self.features_option = Element(browser, By.XPATH, "//*[@value='Deadstock']")
        self.condition_details = Element(browser, By.XPATH, "//*[@name='conditionDetails']")
        self.condition_details_option = Element(browser, By.XPATH, "//*[@value='Slight Edge/Shelf Wear']")
        self.sku = Element(browser, By.XPATH, "//*[@name='sku']")
        self.notes = Element(browser, By.XPATH, "//*[@name='notes']")

        self.add_product_btn = Element(browser, By.XPATH, "//*[text()='Add Product']")
        self.success_message = Element(browser, By.XPATH, "//*[@class='success-message']")

        # this field is required. messages
        self.field_is_required_1 = Element(browser, By.XPATH, "//div[1]/div[2]/div[1]/span")
        self.field_is_required_2 = Element(browser, By.XPATH, "//div[1]/div[3]/div[1]/span")
        self.field_is_required_3 = Element(browser, By.XPATH, "//div[1]/div[4]/div[1]/span")
        self.field_is_required_4 = Element(browser, By.XPATH, "//div[1]/div[1]/div[2]/span")
        self.field_is_required_5 = Element(browser, By.XPATH, "//div[1]/div[2]/div[2]/span")
        self.field_is_required_6 = Element(browser, By.XPATH, "//div[1]/div[3]/div[2]/span")
        self.field_is_required_7 = Element(browser, By.XPATH, "//div[1]/div[4]/div[2]/span")

    def name_input(self, name='Ecco'):
        self.name.enter_text(name)

    def format_input(self):
        self.format.click()
        self.format_option.click()

    def condition_input(self):
        self.cond.click()
        self.cond_option.click()

    def opening_price_input(self, price='1000'):
        self.opening_price.enter_text(price)

    def size_input(self):
        self.size.click()
        self.size_option.click()

    def quantity_input(self, quantity='7'):
        self.quantity.enter_text(quantity)

    def box_condition_input(self):
        self.box_condition.click()
        self.box_condition_option.click()

    def asking_price_input(self, a_price='666'):
        self.asking_price.enter_text(a_price)

        # non required fields

    def release_year_input(self):
        self.release_year.click()
        self.release_year_option.click()

    def country_input(self):
        self.country.click()
        self.country_option.click()

    def brand_input(self, brand='Skorokhod'):
        self.brand.enter_text(brand)

    def colorway_input(self, brand='brown'):
        self.colorway.enter_text(brand)

    def features_input(self):
        self.features.click()
        self.features_option.click()

    def condition_details_input(self):
        self.condition_details.click()
        self.condition_details_option.click()

    def notes_input(self, note='eklmneklmn'):
        self.notes.enter_text(note)

    def sku_input(self, note='eklmneklmn'):
        self.sku.enter_text(note)

    def add_product_btn_click(self):
        self.add_product_btn.click()

    def success_message_check(self):
        self.success_message.wait_until_visible()

        # This field is required. warning pops up

    def this_field_is_required_check(self):
        self.field_is_required_1.wait_until_visible()
        self.field_is_required_2.wait_until_visible()
        self.field_is_required_3.wait_until_visible()
        self.field_is_required_4.wait_until_visible()
        self.field_is_required_5.wait_until_visible()
        self.field_is_required_6.wait_until_visible()
        self.field_is_required_7.wait_until_visible()


