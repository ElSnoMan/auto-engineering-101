from chapters.ch5 import product_page


def test_sort_by_name_from_z_to_a(py, login):
    product_page.sort_products_by(py, 'Name (Z to A)')
    item_names = product_page.get_item_names(py)

    expected_item_names = item_names.copy()
    expected_item_names.sort(reverse=True)
    assert expected_item_names == item_names
