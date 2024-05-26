from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        self.wait_for_visibility_of_element(locator)
        self.driver.find_element(*locator).click()

    def get_text_from_element(self, locator):
        self.wait_for_visibility_of_element(locator)
        return self.driver.find_element(*locator).text

    def set_text_to_field(self, locator, text):
        self.wait_for_visibility_of_element(locator)
        self.driver.find_element(*locator).send_keys(text)

    def scroll_down_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_expected_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
