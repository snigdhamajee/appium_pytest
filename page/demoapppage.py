import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.basetests import BaseTests


class ProductCheckout(BaseTests):
    """
    Page Object for the Landing Page of the app.
    This class contains locators and actions for the landing page.
    """

    # Locators for elements on the Landing Page
    title_element = (By.ID, "com.saucelabs.mydemoapp.android:id/mTvTitle")
    product1 = (By.XPATH, '(//android.widget.ImageView[@content-desc="Product Image"])[1]')
    product_list = (By.ID, "com.saucelabs.mydemoapp.android:id/productIV")
    product_price_list = (By.ID, "com.saucelabs.mydemoapp.android:id/priceTV")
    cart_img = (By.ID, "com.saucelabs.mydemoapp.android:id/cartIV")
    add_to_cart = (By.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    product_highlights = (By.ID, 'com.saucelabs.mydemoapp.android:id/productHeightLightsTV')
    total_price = (By.ID, "com.saucelabs.mydemoapp.android:id/totalPriceTV")
    proceed_to_checkout = (By.ID, "com.saucelabs.mydemoapp.android:id/cartBt")
    user1_email = (By.ID, "com.saucelabs.mydemoapp.android:id/username1TV")
    usermail_placeholder = (By.ID, "com.saucelabs.mydemoapp.android:id/nameET")
    password_placeholder = (By.ID, "com.saucelabs.mydemoapp.android:id/passwordET")
    login_btn = (By.ID, "com.saucelabs.mydemoapp.android:id/loginBtn")
    num_of_product = (By.ID, "com.saucelabs.mydemoapp.android:id/noTV")
    payment_btn = (By.ID, "com.saucelabs.mydemoapp.android:id/paymentBtn")
    error = (By.ID, "com.saucelabs.mydemoapp.android:id/fullNameErrorTV") # Please provide your full name.


    def is_title_present(self):
        """ Check if the title element is present """
        return self.get_element(self.title_element)

    def get_list_of_products(self):
        """ Check if the native button is present """
        return self.get_element_list(self.product_list)

    def click_any_product(self):
        """ Click on the 'Functions' button """
        elements = self.get_element_list(self.product_list)
        random_index = random.randint(0, 2)
        # print(random_index)
        elements[random_index].click()
        return random_index

    def get_list_of_product_price(self):
        return self.get_element_list(self.product_price_list)

    def get_product_page_image(self):
        return self.get_element(self.product_list)

    def get_product_page_price(self):
        return self.get_element(self.product_price_list)

    def scroll_to_add_to_cart(self):
        element = self.get_element(self.add_to_cart)
        self.scroll_to_element(element)

    def click_on_add_to_cart(self):
        element = self.get_element(self.add_to_cart)
        element.click()

    def get_add_to_cart(self):
        element = self.get_element(self.add_to_cart)
        return element

    def get_number_of_product_text(self):
        return self.get_element(self.num_of_product).text

    def click_on_cart(self):
        self.click(self.cart_img)

    def click_on_product(self):
        self.click(self.product1)

    def get_total_price(self):
        return self.get_element(self.total_price)

    def click_on_proceed_to_checkout(self):
        self.click(self.proceed_to_checkout)

    def get_email_text_box(self):
        return self.get_element(self.usermail_placeholder)

    def get_password_text_box(self):
        return self.get_element(self.password_placeholder)

    def click_login_button(self):
        self.click(self.login_btn)

    def click_user_1(self):
        self.click(self.user1_email)

    def get_user1_details(self):
        self.get_element(self.user1_email)

    def get_text_from_email(self):
        element_text = self.get_element(self.usermail_placeholder).text
        return element_text

    def click_payment_btn(self):
        self.click(self.payment_btn)

    def get_payment_btn(self):
        self.get_element(self.payment_btn)

    def get_error_text(self):
        self.get_element(self.error)







