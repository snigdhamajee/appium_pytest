import time

import pytest

from page.demoapppage import ProductCheckout


@pytest.mark.usefixtures("appium_driver")
class TestProduct:

    def test_launch_app(self, appium_driver):
        """
        Verify that the app launches successfully and validates the landing page.
        """
        self.driver = appium_driver
        self.product = ProductCheckout(self.driver)

        assert self.product.is_title_present()
        print("title is present")
        assert self.product.get_list_of_products()
        print("get list of products")
        price_of_product_selected = self.product.get_list_of_product_price()
        price_list = [x.text for x in price_of_product_selected]
        print(price_list)
        self.product.click_any_product()
        assert self.product.get_product_page_image()
        product_page_price = self.product.get_product_page_price().text
        element = self.product.get_add_to_cart()
        self.driver.execute_script("mobile: scrollGesture", {
            "elementId": element,
            "direction": "down",
            "percent": 3.0
        })
        assert self.product.get_add_to_cart()
        number1 = self.product.get_number_of_product_text()
        self.product.click_on_add_to_cart()
        number2 = self.product.get_number_of_product_text()
        assert number2 == number1
        self.product.click_on_cart()
        time.sleep(2)
        assert self.product.get_product_page_price().text == product_page_price
        assert self.product.get_product_page_price().text == self.product.get_total_price().text

        self.product.click_on_proceed_to_checkout()
        assert self.product.get_email_text_box()
        self.product.click_user_1()
        self.product.click_login_button()
        time.sleep(5)

        assert self.product.get_payment_btn()
        self.product.click_payment_btn()
        assert self.product.get_error_text()










