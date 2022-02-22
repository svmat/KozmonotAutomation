from behave import given, when, then
from Pages.left_menu import LeftMenu
from Pages.cargo_bay_page import CargoBay
from Pages.select_product_type_menu import SelectProductType
from Pages.music_add_page import MusicAdd
from browser import Browser
from UIElement import UIElement as Element
from selenium.webdriver.common.by import By

import time

URL = "http://app.kozmonot.tech/"


@given('"Cargo Bay" page downloaded')
def download_cargo_bay_page(context):
    browser = Browser(URL, "chrome")
    context.browser = browser
    # sign in procedure
    sign_in_btn = Element(browser, By.XPATH, "//*[text()='Sign In']")
    sign_in_btn.click()
    user_name = Element(browser, By.XPATH, "//*[@id='id_username']")
    user_name.enter_text("aleknevus@gmail.com")
    password = Element(browser, By.XPATH, "//*[@id='id_password']")
    password.enter_text("Chicago20")
    sign_in_btn = Element(browser, By.XPATH, "//*[@type='submit']")
    sign_in_btn.click()
    # open cargo bay page
    left_menu = LeftMenu(context.browser)
    left_menu.click_cargo_bay_btn()
    cargo_bay = CargoBay(context.browser)
    assert cargo_bay.title_of_page_get_title() == 'Cargo Bay'
    context.cargo_bay = cargo_bay
    # browser.shutdown()


@when('user click "Add new product" button')
def add_new_product_btn(context):
    cargo_bay = context.cargo_bay
    cargo_bay.click_add_new_product_btn()
    # time.sleep(2)


@when('user open new  "{field}" item page')
def open_new_product_page(context, field):
    select_product_type = SelectProductType(context.browser)
    if field == "music":
        select_product_type.click_music_btn()

    elif field == "film":
        select_product_type.click_film_btn()

    elif field == "card":
        select_product_type.click_cards_btn()
    elif field == "shoes":
        select_product_type.click_shoe_btn()
    #time.sleep(1)


@when('enter data in "{field}" required fields')
def requred_fields_input(context, field):
    music_add = MusicAdd(context.browser)
    if field == "music":
        music_add.artist_name_input()
        music_add.opening_price_input()
        music_add.album_name_input()
        music_add.quantity_input()
        music_add.product_format_input()
        music_add.media_condition_input()
        music_add.sleeve_cond_input()
        music_add.asking_price_input()
        time.sleep(3)

    context.music_add = music_add


@when('click "Add product" "{field}" button')
def add_product_btn(context, field):
    music_add = context.music_add
    if field == "music":
        music_add.add_product_btn_click()

    time.sleep(2)



@then('New "{field}" item was created warning pops up')
def new_item_created_verify(context, field):
    if field == "music":
        music_add = context.music_add
        music_add.success_message_check()

    elif field == "film":
        pass
    elif field == "card":
        pass
    elif field == "shoes":
        pass


@when('enter data in "{field}" all non required fields')
def non_required_fields_input(context, field):
    pass


@then('"This field is required" warnings pops up under all "{field}" required fields')
def requred_fields_warning(context, field):
    pass
