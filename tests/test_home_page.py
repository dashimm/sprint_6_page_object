import allure
import pytest
from helpers.test_data import AnswersListFaq, Urls
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage
from conftest import driver


class TestFAQHomePage:
    @allure.title('Проверка ответов на вопросы в выпадающем списке раздела FAQ')
    @pytest.mark.parametrize('QUESTIONS_LIST, ANSWERS_LIST, answers_text_list',
                             zip(HomePageLocators.QUESTIONS_LIST, HomePageLocators.ANSWERS_LIST,
                                 AnswersListFaq.answers_text_list))
    def test_faq_question_return_answers(self, driver, QUESTIONS_LIST, ANSWERS_LIST, answers_text_list):
        home_page = HomePage(driver)
        home_page.get_cookies()
        home_page.scroll_down_page()
        actual_answers_text = home_page.get_text_of_questions(QUESTIONS_LIST, ANSWERS_LIST)
        assert actual_answers_text == answers_text_list


class TestHomePageLogo:
    @allure.title('Клик на лого Самоката в хэдере ведет на главную страницу Самоката')
    def test_click_on_scooter_logo(self, driver):
        home_page = HomePage(driver)
        home_page.click_on_order_but_from_header()
        home_page.click_on_scooter_logo()
        current_url = Urls.HOME_PAGE_URL
        assert current_url == home_page.get_current_url()

    @allure.title('Клик на лого Яндекса в хэдере ведет на главную страницу Dzen.ru')
    def test_click_on_yandex_logo(self, driver):
        home_page = HomePage(driver)
        dzen_page = Urls.DZEN_HOME_PAGE
        home_page.click_on_yandex_logo()
        home_page.switch_to_new_tab()
        home_page.wait_expected_url(dzen_page)
        assert dzen_page == home_page.get_current_url()
