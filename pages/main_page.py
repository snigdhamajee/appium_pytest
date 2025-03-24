import pytest
from selenium.webdriver.common.by import By


class MainMenuPage:
    """
    Page object for the Main Menu (com.testdroid.sample.android.MM_MainMenu)
    """

    # Locators
    app_title = (By.ID, "com.testdroid.sample.android:id/mm_iv_title")
    native_btn = (By.ID, "com.testdroid.sample.android:id/mm_b_native")

    def __init__(self, driver):
        """
        Initialize the Main Menu page.
        :param driver: The Appium driver instance.
        """
        self.driver = driver

    def get_app_title(self):
        return self.driver.find_element(*self.app_title)

    def get_native_btn(self):
        return self.driver.find_element(*self.native_btn)