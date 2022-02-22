from UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class SelectProductType:
    def __init__(self, browser):
        self.media_btn = Element(browser, By.XPATH, "//*[text()='Media']")
        self.cards_btn = Element(browser, By.XPATH, "//*[text()='Cards']")
        self.shoe_btn = Element(browser, By.XPATH, "//*[text()='Shoe']")
        self.gaming_btn = Element(browser, By.XPATH, "//*[text()='Gaming']")
        self.comics_btn = Element(browser, By.XPATH, "//*[text()='Comics']")
        self.apparel_btn = Element(browser, By.XPATH, "//*[text()='Apparel']")
        self.music_btn = Element(browser, By.XPATH, "//*[text()='Music']")
        self.film_btn = Element(browser, By.XPATH, "//*[text()='Film']")

    def click_media_btn(self):
        self.media_btn.click()

    def click_cards_btn(self):
        self.cards_btn.click()

    def click_shoe_btn(self):
        self.shoe_btn.click()

    def click_gaming_btn(self):
        self.gaming_btn_btn.click()

    def click_comics_btn(self):
        self.comics_btn_btn.click()

    def click_apparel_btn(self):
        self.apparel_btn.click()

    def click_music_btn(self):
        self.media_btn.click()
        self.music_btn.click()

    def click_film_btn(self):
        self.media_btn.click()
        self.film_btn.click()
