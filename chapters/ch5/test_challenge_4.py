import chapters.ch5.swag_actions as swag


def test_checkout_success_with_single_item(py, login):
    swag.add_first_item_to_cart(py)
    swag.start_checkout(py)
    swag.enter_shipping_info(py, 'Carlos', 'Kidman', '84042')
    swag.confirm_checkout(py)
    assert py.contains('THANK YOU FOR YOUR ORDER')
