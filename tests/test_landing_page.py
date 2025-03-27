import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.pageobjects import LandingPage
from tests.conftest import appium_driver


@pytest.mark.usefixtures("appium_driver")
class TestLandingPage:

    # def setup(self, method):
    #     pass

    # def test_launch_app(self, appium_driver):
    #     """
    #     Verify that the app launches and the landing page is validated
    #     """
    #     self.driver = appium_driver
    #     assert self.driver.find_element(By.ID, "com.testdroid.sample.android:id/mm_iv_title")
    #     # assert self.driver.find_element(By.ID, "com.testdroid.sample.android:id/mm_b_native")
    #     # function1 = self.driver.find_element(By.ID, "com.testdroid.sample.android:id/mm_b_functions")
    #     # function1.click()
    #     # # WebDriverWait.until(EC.presence_of_element_located(By.ID, self.function))
    #     # # assert self.driver.find_element(By.ID, self.function).text == "Functions"

    def test_launch_app_with_pom(self, appium_driver):
        """
        Verify that the app launches successfully and validates the landing page.
        """
        self.driver = appium_driver
        self.landing_page = LandingPage(self.driver)

        assert self.landing_page.is_title_present(), "Title element not found!"

        assert self.landing_page.is_native_button_present(), "Native button not found!"

        assert self.landing_page.is_title_visible()

        self.landing_page.click_functions_button()

        assert self.landing_page.get_function_text() == "Functions", "Failed to navigate to Functions page!"

        self.driver.back()

        assert self.landing_page.is_title_present()

        self.landing_page.click_hybrid()

        time.sleep(5)

        self.landing_page.switch_to_webview()
        assert self.landing_page.get_hybrid_body() == "Google"




