from behave import given, when, then
from Pages.left_menu import LeftMenu
from Pages.cargo_bay_page import CargoBay
from Pages.select_product_type_menu import SelectProductType
from Pages.music_add_page import MusicAdd
from Pages.film_add_page import FilmAdd
from Pages.card_add_page import CardAdd
from Pages.shoes_add_page import ShoesAdd
from browser import Browser
from UIElement import UIElement as Element
from selenium.webdriver.common.by import By


import time

URL = "http://app.kozmonot.tech/"


@given('"Cargo Bay" page loaded')
def load_cargo_bay_page(context):
    browser = Browser(URL, "remote")
    context.browser = browser
    # sign in procedure
    sign_in_btn = Element(browser, By.XPATH, "//*[text()='Sign In']")
    sign_in_btn.click()
    user_name = Element(browser, By.XPATH, "//*[@id='id_username']")
    user_name.enter_text("qwerty34@gmail.com")
    password = Element(browser, By.XPATH, "//*[@id='id_password']")
    password.enter_text("Avz#3435")
    sign_in_btn = Element(browser, By.XPATH, "//*[@type='submit']")
    sign_in_btn.click()
    # open cargo bay page
    left_menu = LeftMenu(context.browser)
    left_menu.click_cargo_bay_btn()
    cargo_bay = CargoBay(context.browser)
    assert cargo_bay.title_of_page_get_title() == 'Cargo Bay'
    context.cargo_bay = cargo_bay


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
    # time.sleep(1)


@when('enter data in "{field}" required fields')
def required_fields_input(context, field):
    if field == "music":
        music_add = MusicAdd(context.browser)
        music_add.media_condition_input()
        music_add.product_format_input()
        music_add.artist_name_input()
        music_add.opening_price_input()
        music_add.album_name_input()
        music_add.quantity_input()
        music_add.sleeve_cond_input()
        music_add.asking_price_input()
        context.music_add = music_add

    elif field == "film":
        film_add = FilmAdd(context.browser)
        film_add.title_input()
        film_add.film_condition_input()
        film_add.opening_price_input()
        film_add.product_format_input()
        film_add.quantity_input()
        film_add.asking_price_input()
        film_add.sleeve_cond_input()
        context.film_add = film_add

    elif field == "card":
        card_add = CardAdd(context.browser)
        card_add.card_name_input()
        card_add.format_input()
        card_add.condition_input()
        card_add.opening_price_input()
        card_add.card_number_input()
        card_add.quantity_input()
        card_add.category_input()
        card_add.asking_price_input()
        context.card_add = card_add

    elif field == "shoes":
        shoes_add = ShoesAdd(context.browser)
        shoes_add.name_input()
        shoes_add.format_input()
        shoes_add.condition_input()
        shoes_add.opening_price_input()
        shoes_add.size_input()
        shoes_add.quantity_input()
        shoes_add.box_condition_input()
        shoes_add.asking_price_input()
        context.shoes_add = shoes_add



@when('click "Add product" "{field}" button')
def add_product_btn(context, field):
    if field == "music":
        music_add = MusicAdd(context.browser)
        music_add.add_product_btn_click()
        context.music_add = music_add

    elif field == "film":
        film_add = FilmAdd(context.browser)
        film_add.add_product_btn_click()
        context.film_add = film_add

    elif field == "card":
        card_add = CardAdd(context.browser)
        card_add.add_product_btn_click()
        context.card_add = card_add

    elif field == "shoes":
        shoes_add = ShoesAdd(context.browser)
        shoes_add.add_product_btn_click()
        context.shoes_add = shoes_add

@then('New "{field}" item was created warning pops up')
def new_item_created_verify(context, field):
    if field == "music":
        music_add = context.music_add
        music_add.success_message_check()

    elif field == "film":
        film_add = context.film_add
        film_add.success_message_check()

    elif field == "card":
        card_add = context.card_add
        card_add.success_message_check()

    elif field == "shoes":
        shoes_add = ShoesAdd(context.browser)
        shoes_add.success_message_check()

    context.browser.shutdown()



@when('enter data in "{field}" all non required fields')
def non_required_fields_input(context, field):
    if field == "music":
        music_add = context.music_add
        music_add.label_input()
        music_add.catalog_number_input()
        music_add.discogs_link_input()
        music_add.notes_input()
        music_add.press_input()
        music_add.category_input()
        music_add.release_year_input()
        music_add.country_input()
        music_add.condition_details_input()
        music_add.features_input()

    elif field == "film":
        film_add = FilmAdd(context.browser)
        film_add.release_year_input()
        film_add.country_input()
        film_add.features_input()
        film_add.publisher_input()
        film_add.condition_details_input()
        film_add.name_input()
        film_add.notes_input()
        context.film_add = film_add

    elif field == "card":
        card_add = CardAdd(context.browser)
        card_add.release_year_input()
        card_add.country_input()
        card_add.brand_input()
        card_add.graded_input()
        card_add.features_input()
        card_add.condition_details_input()
        card_add.official_grade_input()
        card_add.notes_input()
        card_add.sku_input()
        context.card_add = card_add

    elif field == "shoes":
        shoes_add = ShoesAdd(context.browser)
        shoes_add.release_year_input()
        shoes_add.country_input()
        shoes_add.brand_input()
        shoes_add.colorway_input()
        shoes_add.features_input()
        shoes_add.condition_details_input()
        shoes_add.notes_input()
        shoes_add.sku_input()
        context.shoes_add = shoes_add


@then('"This field is required" warnings pops up under all "{field}" required fields')
def required_fields_warning(context, field):
    if field == 'music':
        music_add = context.music_add
        music_add.this_field_is_required_check()

    elif field == 'film':
        film_add = context.film_add
        film_add.this_field_is_required_check()

    elif field == 'card':
        card_add = context.card_add
        card_add.this_field_is_required_check()

    elif field == "shoes":
        shoes_add = context.shoes_add
        shoes_add.this_field_is_required_check()

    context.browser.shutdown()
