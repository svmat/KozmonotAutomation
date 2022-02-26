from UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class CardAdd:
    def __init__(self, browser):
        # required fields
        self.card_name = Element(browser, By.XPATH, "//*[@name='cardName']")
        self.format = Element(browser, By.XPATH, "//*[@name='productFormat']")
        self.format_option = Element(browser, By.XPATH, "//*[@value='Card']")
        self.cond = Element(browser, By.XPATH, "//*[@name='condition']")
        self.cond_option = Element(browser, By.XPATH, "//*[@value='GEM']")
        self.opening_price = Element(browser, By.XPATH, "//*[@name='openingPrice']")
        self.card_number = Element(browser, By.XPATH, "//*[@name='cardNumber']")
        self.quantity = Element(browser, By.XPATH, "//*[@name='quantity']")
        self.category = Element(browser, By.XPATH, "//*[@name='category']")
        self.category_option = Element(browser, By.XPATH, "//*[@value='Baseball']")
        self.asking_price = Element(browser, By.XPATH, "//*[@name='askingPrice']")

        #non required fiefls
        self.release_year = Element(browser, By.XPATH, "//*[@name='releaseYear']")
        self.release_year_option = Element(browser, By.XPATH, "//*[@value='2022']")
        self.country = Element(browser, By.XPATH, "//*[@name='country']")
        self.country_option = Element(browser, By.XPATH, "//*[@value='Afghanistan']")
        self.brand = Element(browser, By.XPATH, "//*[@name='brand']")
        self.graded = Element(browser, By.XPATH, "//*[@name='graded']")
        self.graded_option = Element(browser, By.XPATH, "//*[@value='PSA']")
        self.features = Element(browser, By.XPATH, "//*[@name='features']")
        self.features_option = Element(browser, By.XPATH, "//*[@value='All-Star']")
        self.condition_details = Element(browser, By.XPATH, "//*[@name='conditionDetails']")
        self.condition_details_option = Element(browser, By.XPATH, "//*[@value='Slight Edge/Shelf Wear']")
        self.official_grade = Element(browser, By.XPATH, "//*[@name='officialGrade']")
        self.official_grade_option = Element(browser, By.XPATH, "//*[@value='10']")
        self.sku = Element(browser, By.XPATH, "//*[@name='sku']")
        self.notes = Element(browser, By.XPATH, "//*[@name='notes']")

        self.add_product_btn = Element(browser, By.XPATH, "//*[text()='Add Product']")
        self.success_message = Element(browser, By.XPATH, "//*[@class='success-message']")

        # this field is required. messages
        self.field_is_required_1 = Element(browser, By.XPATH, "//div[1]/div[2]/div[1]/span")
        self.field_is_required_2 = Element(browser, By.XPATH, "//div[1]/div[3]/div[1]/span")
        self.field_is_required_3 = Element(browser, By.XPATH, "//div[1]/div[4]/div[1]/span")
        self.field_is_required_4 = Element(browser, By.XPATH, "//div[1]/div[2]/div[2]/span")
        self.field_is_required_5 = Element(browser, By.XPATH, "//div[1]/div[4]/div[2]/span")

        # required fields
    def card_name_input(self, name='Terminator'):
        self.card_name.enter_text(name)

    def format_input(self):
        self.format.click()
        self.format_option.click()

    def condition_input(self):
        self.cond.click()
        self.cond_option.click()

    def opening_price_input(self, price='1000'):
        self.opening_price.enter_text(price)

    def card_number_input(self, card_num='12345'):
        self.card_number.enter_text(card_num)

    def quantity_input(self, quantity='7'):
        self.quantity.enter_text(quantity)

    def category_input(self):
        self.category.click()
        self.category_option.click()

    def asking_price_input(self, a_price='666'):
        self.asking_price.enter_text(a_price)

    # non required fields

    def release_year_input(self):
        self.release_year.click()
        self.release_year_option.click()

    def country_input(self):
        self.country.click()
        self.country_option.click()

    def brand_input(self, brand='USSR'):
        self.brand.enter_text(brand)

    def graded_input(self):
        self.graded.click()
        self.graded_option.click()

    def features_input(self):
        self.features.click()
        self.features_option.click()

    def condition_details_input(self):
        self.condition_details.click()
        self.condition_details_option.click()

    def official_grade_input(self):
        self.official_grade.click()
        self.official_grade_option.click()

    def notes_input(self, note='hdsfiudhfdsakj'):
        self.notes.enter_text(note)

    def sku_input(self, note='hdsfiudhfdsakj'):
        self.sku.enter_text(note)

    def add_product_btn_click(self):
        self.add_product_btn.click()

    def success_message_check(self):
        self.success_message.wait_until_visible()

    #This field is required. warning pops up

    def this_field_is_required_check(self):
        self.field_is_required_1.wait_until_visible()
        self.field_is_required_2.wait_until_visible()
        self.field_is_required_3.wait_until_visible()
        self.field_is_required_4.wait_until_visible()
        self.field_is_required_5.wait_until_visible()









