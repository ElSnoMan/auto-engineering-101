import pytest

from chapters.ch5.swag_actions import login_with


def test_user_can_login(py, login):
    assert py.contains('Products')


def test_user_can_logout(py, login):
    py.contains('Open Menu').click()
    py.contains('Logout').click(force=True)
    assert py.should().contain_url('index.html')


examples = [
    ('fake', 'secret_sauce', 'Username and password do not match any user in this service'),
    ('standard_user', 'fake', 'Username and password do not match any user in this service'),
    ('', 'secret_sauce', 'Username is required'),
    ('standard_user', '', 'Password is required')
]


@pytest.mark.parametrize('username, password, error', examples)
def test_user_cannot_login_with_invalid_credentials(py, username, password, error):
    login_with(py, username, password)
    assert py.get('[data-test="error"]').should().contain_text(error)
