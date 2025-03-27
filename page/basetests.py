from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTests:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        self.get_element(locator).click()

    def get_element(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator)
        )

    def send_keys(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def is_visible(self, locator):
        return self.driver.find_element(*locator)

    def get_element_list(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(locator)
        )

    def scroll_to_element(self, element):
        element = self.driver.find_element(element)
        self.driver.execute_script("mobile: scroll", {"element": element, "toVisible": True})

    def touch_action(self, element):
        element = self.driver.find_element(*element)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click(element)
        actions.perform()

    def switch_to_webview(self):
        contexts_available = self.driver.contexts
        print(contexts_available)
        for context in contexts_available:
            if "WEBVIEW" in context:
                self.driver.switch_to.context(context)
                print(f"Switched to {context}")
                break
        else:
            raise Exception("No WebView context found!")





