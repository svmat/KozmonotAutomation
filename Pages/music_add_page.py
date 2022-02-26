from UIElement import UIElement as Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class MusicAdd:
    def __init__(self, browser):
        # required fields
        self.artist_name = Element(browser, By.XPATH, "//*[@name='artistName']")
        self.opening_price = Element(browser, By.XPATH, "//*[@name='openingPrice']")
        self.album_name = Element(browser, By.XPATH, "//*[@name='albumName']")
        self.quantity = Element(browser, By.XPATH, "//*[@name='quantity']")
        # requred fields with submenus
        self.product_format = Element(browser, By.XPATH, "//*[@name='productFormat']")
        self.product_format_option = Element(browser, By.XPATH, "//*[@value='Vinyl']")
        self.media_cond = Element(browser, By.XPATH, "//*[@name='condition']")
        self.media_cond_option = Element(browser, By.XPATH, "//*[@value='MT']")
        self.sleeve_cond = Element(browser, By.XPATH, "//*[@name='sleeveCondition']")
        self.sleeve_cond_option = Element(browser, By.XPATH, "//*[@value='SLD']")
        self.asking_price = Element(browser, By.XPATH, "//*[@name='askingPrice']")
        # non required fields
        self.label = Element(browser, By.XPATH, "//*[@name='label']")
        self.catalog_number = Element(browser, By.XPATH, "//*[@name='catalogNumber']")
        self.discogs_link = Element(browser, By.XPATH, "//*[@name='discogsLink']")
        self.notes = Element(browser, By.XPATH, "//*[@name='notes']")
        # non required fields with submenus
        self.press = Element(browser, By.XPATH, "//*[@name='press']")
        self.press_option = Element(browser, By.XPATH, "//*[@value='OG']")
        self.category = Element(browser, By.XPATH, "//*[@name='category']")
        self.category_option = Element(browser, By.XPATH, "//*[@value='LP']")
        self.release_year = Element(browser, By.XPATH, "//*[@name='releaseYear']")
        self.release_year_option = Element(browser, By.XPATH, "//*[@value='2022']")
        self.country = Element(browser, By.XPATH, "//*[@name='country']")
        self.country_option = Element(browser, By.XPATH, "//*[@value='Afghanistan']")
        self.condition_details = Element(browser, By.XPATH, "//*[@name='conditionDetails']")
        self.condition_details_option = Element(browser, By.XPATH, "//*[@value='Slight Edge/Shelf Wear']")
        self.features = Element(browser, By.XPATH, "//*[@name='features']")
        self.features_option = Element(browser, By.XPATH, "//*[@value='Club Pressing']")

        self.add_product_btn = Element(browser, By.XPATH, "//*[text()='Add Product']")
        self.success_message = Element(browser, By.XPATH, "//*[@class='success-message']")
        #this field is required. messages
        self.field_is_required_1 = Element(browser, By.XPATH, "//div[1]/div[1]/div[1]/span")
        self.field_is_required_2 = Element(browser, By.XPATH, "//div/div[2]/div/span")
        self.field_is_required_3 = Element(browser, By.XPATH, "//div/div[3]/div/span")
        self.field_is_required_4 = Element(browser, By.XPATH, "//div/div[4]/div/span")
        self.field_is_required_5 = Element(browser, By.XPATH, "//div[1]/div[1]/div[2]/span")
        self.field_is_required_6 = Element(browser, By.XPATH, "//div/div[1]/div[2]/div[2]/span")
        self.field_is_required_7 = Element(browser, By.XPATH, "//div[1]/div[3]/div[2]/span")
        self.field_is_required_8 = Element(browser, By.XPATH, "//div[1]/div[4]/div[2]/span")

    # required fields functions

    def artist_name_input(self, name='John S'):
        self.artist_name.enter_text(name)

    def opening_price_input(self, price='10'):
        self.opening_price.enter_text(price)

    def album_name_input(self, album='Album77'):
        self.album_name.enter_text(album)

    def quantity_input(self, quantity='7'):
        self.quantity.enter_text(quantity)

    def product_format_input(self):
        self.product_format.click()
        self.product_format_option.click()

    def media_condition_input(self):
        self.media_cond.click()
        self.media_cond_option.click()

    def sleeve_cond_input(self):
        self.sleeve_cond.click()
        self.sleeve_cond_option.click()

    def asking_price_input(self, a_price='20'):
        self.asking_price.enter_text(a_price)

        # non required fields

    def label_input(self, label='Label22'):
        self.label.enter_text(label)

    def catalog_number_input(self, cat_num='12345'):
        self.catalog_number.enter_text(cat_num)

    def discogs_link_input(self, disc_link='rewrewrwerwq'):
        self.discogs_link.enter_text(disc_link)

    def notes_input(self, note='hdsfiudhfdsakj'):
        self.notes.enter_text(note)

    def press_input(self):
        self.press.click()
        self.press_option.click()

    def category_input(self):
        self.category.click()
        self.category_option.click()

    def release_year_input(self):
        self.release_year.click()
        self.release_year_option.click()

    def country_input(self):
        self.country.click()
        self.country_option.click()

    def condition_details_input(self):
        self.condition_details.click()
        self.condition_details_option.click()

    def features_input(self):
        self.features.click()
        self.features_option.click()

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
        self.field_is_required_6.wait_until_visible()
        self.field_is_required_7.wait_until_visible()
        self.field_is_required_8.wait_until_visible()


