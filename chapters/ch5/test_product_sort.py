from chapters.ch5 import product_page


def test_sort_by_name_from_z_to_a(py, login):
    product_page.sort_products_by(py, 'Name (Z to A)')
    item_names = product_page.get_item_names(py)

    expected_item_names = item_names.copy()
    expected_item_names.sort(reverse=True)
    assert expected_item_names == item_names


def test_sort_by_name_from_a_to_z(py, login):
    product_page.sort_products_by(py, 'Name (A to Z)')
    item_names = product_page.get_item_names(py)

    expected_item_names = item_names.copy()
    expected_item_names.sort(reverse=False)
    assert expected_item_names == item_names


def test_sort_by_price_from_low_to_high(py, login):
    product_page.sort_products_by(py, 'Price (low to high)')
    item_prices = product_page.get_item_prices(py)

    expected_item_prices = item_prices.copy()
    expected_item_prices.sort(reverse=False)
    assert expected_item_prices == item_prices


def test_sort_by_price_from_high_to_low(py, login):
    product_page.sort_products_by(py, 'Price (high to low)')
    item_prices = product_page.get_item_prices(py)

    expected_item_prices = item_prices.copy()
    expected_item_prices.sort(reverse=True)
    assert expected_item_prices == item_prices
