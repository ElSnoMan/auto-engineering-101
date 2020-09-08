import pytest


def test_user_can_login(py):
    py.visit('http://saucedemo.com')
    py.get('#user-name').type('standard_user')
    py.get('#password').type('secret_sauce')
    py.get('#login-button').click()
    assert py.contains('Products')


def test_user_can_logout(py):
    py.visit('http://saucedemo.com')
    py.get('#user-name').type('standard_user')
    py.get('#password').type('secret_sauce')
    py.get('#login-button').click()
    py.contains('Open Menu').click()
    py.contains('Logout').click(force=True)
    assert py.should().contain_url('index.html')


def test_user_cannot_login_with_invalid_credentials(py):
    py.visit('http://saucedemo.com')
    py.get('#user-name').type('')
    py.get('#password').type('secret_sauce')
    py.get('#login-button').click()
    assert py.get('[data-test="error"]').should().contain_text('Username is required')
