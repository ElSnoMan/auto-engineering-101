def login_with(py, username, password):
    py.visit('http://saucedemo.com')
    py.get('#user-name').type(username)
    py.get('#password').type(password)
    py.get('#login-button').click()


def add_first_item_to_cart(py):
    py.contains('ADD TO CART').click()


def start_checkout(py):
    py.get('#shopping_cart_container > a').click()
    py.contains('CHECKOUT').click()


def enter_shipping_info(py, first_name, last_name, postal_code):
    py.get('#first-name').type(first_name)
    py.get('#last-name').type(last_name)
    py.get('#postal-code').type(postal_code)
    py.get('[value="CONTINUE"]').click()


def confirm_checkout(py):
    py.contains('FINISH').click()
