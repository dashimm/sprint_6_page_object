import allure
from pages.base_page import BasePage
from locators.home_page_locators import HeaderLocators, HomePageLocators


class HomePage(BasePage):

    @allure.step('Клик на вопрос в разделе FAQ')
    def click_to_question(self, QUESTIONS_LIST):
        self.wait_for_visibility_of_element(QUESTIONS_LIST)
        self.click_to_element(QUESTIONS_LIST)

    @allure.step('Получение ответа на вопрос в разделе FAQ')
    def get_text_of_questions(self, QUESTIONS_LIST, ANSWERS_LIST):
        self.click_to_question(QUESTIONS_LIST)
        self.wait_for_visibility_of_element(ANSWERS_LIST)
        answers_text = self.get_text_from_element(ANSWERS_LIST)
        return answers_text

    @allure.step('Клик на лого Яндекс')
    def click_on_yandex_logo(self):
        self.click_to_element(HeaderLocators.YANDEX_LOGO)

    @allure.step('Клик на лого Самокат')
    def click_on_scooter_logo(self):
        self.click_to_element(HeaderLocators.SCOOTER_LOGO)

    def get_cookies(self):
        self.wait_for_visibility_of_element(HomePageLocators.COOKIE_BUT)
        self.click_to_element(HomePageLocators.COOKIE_BUT)

    @allure.step('Клик на кнопку Заказать в хэдере')
    def click_on_order_but_from_header(self):
        self.click_to_element(HeaderLocators.ORDER_BUT_HEADER)