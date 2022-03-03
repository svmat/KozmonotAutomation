from UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class FilmAdd:
    def __init__(self, browser):
        # required fields
        self.title = Element(browser, By.XPATH, "//*[@name='title']")
        self.film_cond = Element(browser, By.XPATH, "//*[@name='condition']")
        self.film_cond_option = Element(browser, By.XPATH, "//*[@value='MT']")
        self.opening_price = Element(browser, By.XPATH, "//*[@name='openingPrice']")
        self.format = Element(browser, By.XPATH, "//*[@name='productFormat']")
        self.format_option = Element(browser, By.XPATH, "//*[@value='VHS']")
        self.quantity = Element(browser, By.XPATH, "//*[@name='quantity']")
        self.asking_price = Element(browser, By.XPATH, "//*[@name='askingPrice']")
        self.sleeve_cond = Element(browser, By.XPATH, "//*[@name='sleeveCondition']")
        self.sleeve_cond_option = Element(browser, By.XPATH, "//*[@value='SLD']")

        # non required fields
        self.release_year = Element(browser, By.XPATH, "//*[@name='releaseYear']")
        self.release_year_option = Element(browser, By.XPATH, "//*[@value='2022']")
        self.country = Element(browser, By.XPATH, "//*[@name='country']")
        self.country_option = Element(browser, By.XPATH, "//*[@value='Afghanistan']")
        self.features = Element(browser, By.XPATH, "//*[@name='features']")
        self.features_option = Element(browser, By.XPATH, "//*[@value='Club Pressing']")
        self.publisher = Element(browser, By.XPATH, "//*[@name='publisher']")
        self.condition_details = Element(browser, By.XPATH, "//*[@name='conditionDetails']")
        self.condition_details_option = Element(browser, By.XPATH, "//*[@value='Slight Edge/Shelf Wear']")
        self.name = Element(browser, By.XPATH, "//*[@name='upc']")
        self.notes = Element(browser, By.XPATH, "//*[@name='notes']")

        self.add_product_btn = Element(browser, By.XPATH, "//*[text()='Add Product']")
        self.success_message = Element(browser, By.XPATH, "//*[@class='success-message']")

        self.field_is_required_1 = Element(browser, By.XPATH, "//div[1]/div[1]/div/span")
        self.field_is_required_2 = Element(browser, By.XPATH, "//div[1]/div[2]/div[1]/span")
        self.field_is_required_3 = Element(browser, By.XPATH, "//div[1]/div[3]/div/span")
        self.field_is_required_4 = Element(browser, By.XPATH, "//div[1]/div[4]/div[1]/span")
        self.field_is_required_5 = Element(browser, By.XPATH, "//div[1]/div[2]/div[2]/span")
        self.field_is_required_6 = Element(browser, By.XPATH, "//div[1]/div[4]/div[2]/span")

    # required fields

    def title_input(self, name='True Detective 1'):
        self.title.enter_text(name)

    def film_condition_input(self):
        self.film_cond.click()
        self.film_cond_option.click()

    def opening_price_input(self, price='10'):
        self.opening_price.enter_text(price)

    def product_format_input(self):
        self.format.click()
        self.format_option.click()

    def quantity_input(self, quantity='7'):
        self.quantity.enter_text(quantity)

    def asking_price_input(self, a_price='20'):
        self.asking_price.enter_text(a_price)

    def sleeve_cond_input(self):
        self.sleeve_cond.click()
        self.sleeve_cond_option.click()

    # non required fields

    def release_year_input(self):
        self.release_year.click()
        self.release_year_option.click()

    def country_input(self):
        self.country.click()
        self.country_option.click()

    def features_input(self):
        self.features.click()
        self.features_option.click()

    def publisher_input(self, name='20 century FOX'):
        self.publisher.enter_text(name)

    def condition_details_input(self):
        self.condition_details.click()
        self.condition_details_option.click()

    def name_input(self, name='rtryuryt'):
        self.name.enter_text(name)

    def notes_input(self, note='hdsfiudhfdsakj'):
        self.notes.enter_text(note)

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
