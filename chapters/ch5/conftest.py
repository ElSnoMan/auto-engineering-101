import pytest

from chapters.ch5.swag_actions import login_with


@pytest.fixture
def login(py):
    login_with(py, 'standard_user', 'secret_sauce')
