from behave import given, when, then


@given('"Product" page downloaded')
def download_product_page(context):
    pass


@when('user click "Add new product" button')
def add_new_product_btn(context):
    pass


@when('user open new  "{field}" item page')
def open_new_product_page(context, field):
    if field == "music":
        pass
    elif field == "film":
        pass
    elif field == "card":
        pass
    elif field == "shoes":
        pass


@when('enter data in required fields')
def requred_fields_input(context):
    pass


@when('click "Add product" button')
def add_product_btn(context):
    pass


@then('New "{field}" item was created warning pops up')
def new_item_created_verify(context, field):
    if field == "music":
        pass
    elif field == "film":
        pass
    elif field == "card":
        pass
    elif field == "shoes":
        pass


@when('enter data in all non required fields')
def non_required_fields_input(context):
    pass


@then('"This field is required" warnings pops up under all required fields')
def requred_fields_warning(context):
    pass
