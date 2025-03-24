import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("appium_driver")
class TestLandingPage:

    def test_launch_app(self, appium_driver):
        """
        Verify that the app launches and the landing page is validated
        """
        self.driver = appium_driver
        self.driver.launch_app()
        assert self.driver.find_element(By.ID, "com.testdroid.sample.android:id/mm_iv_title")
        assert self.driver.find_element(By.ID, "com.testdroid.sample.android:id/mm_b_native")
