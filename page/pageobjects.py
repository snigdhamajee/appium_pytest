from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.basetests import BaseTests


class LandingPage(BaseTests):
    """
    Page Object for the Landing Page of the app.
    This class contains locators and actions for the landing page.
    """

    # Locators for elements on the Landing Page
    title_element = (By.ID, "com.testdroid.sample.android:id/mm_iv_title")
    native_button = (By.ID, "com.testdroid.sample.android:id/mm_b_native")
    functions_button = (By.ID, "com.testdroid.sample.android:id/mm_b_functions")
    function_text = (By.ID, "android:id/action_bar_title")
    hybrid_button = (By.ID, "com.testdroid.sample.android:id/mm_b_hybrid")
    hybrid_body = (By.ID, 'android:id/action_bar_title')
    google_link = (By.ID, "com.testdroid.sample.android:id/hy_et_url")

    def is_title_present(self):
        """ Check if the title element is present """
        return self.get_element(self.title_element)

    def is_native_button_present(self):
        """ Check if the native button is present """
        return self.get_element(self.native_button)

    def click_functions_button(self):
        """ Click on the 'Functions' button """
        self.click(self.functions_button)

    def get_function_text(self):
        """ Get the text from the function title after navigation """
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.function_text, "Functions")
        )
        return self.get_element(self.function_text).text

    def is_title_visible(self):
        return self.is_visible(self.title_element)

    def click_hybrid(self):
        self.click(self.hybrid_button)

    def is_google_link_visible(self):
        return self.is_visible(self.google_link)

    def get_hybrid_body(self):
        title = self.driver.execute_script("return document.title")
        print(title )
        return title # Check if WebView is accessible




