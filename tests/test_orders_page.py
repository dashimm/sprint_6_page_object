import allure
from conftest import driver
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.order_page_locators import OrderPageLocators
from helpers.test_data import Users


class TestOrderPage:
    @allure.title('Успешное оформление заказа через кнопку "Заказать" в хэдере главной страницы')
    def test_order_scooter_from_header_button(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.get_cookies()
        order_page.click_on_order_but_from_header()
        order_page.order_scooter(Users.NAME[0],
                                 Users.SURNAME[0],
                                 Users.ADDRESS[0],
                                 OrderPageLocators.CHOOSE_SUBWAY1,
                                 Users.PHONE_NUMBER[0],
                                 OrderPageLocators.CHOOSE_DELIVERY_DATE1,
                                 OrderPageLocators.RENT_TIME_CHOOSE1,
                                 OrderPageLocators.COLOUR_OF_SCOOTER_CHOOSE,
                                 Users.COMMENT[0])
        actual_text = order_page.check_success_order()
        assert 'Заказ оформлен' in actual_text

    @allure.title('Успешное оформление заказа через кнопку "Заказать" внизу главной страницы')
    def test_order_scooter_from_under_button(self, driver):
        home_page = HomePage(driver)
        order_page = OrderPage(driver)
        home_page.get_cookies()
        order_page.click_on_order_but_from_under()
        order_page.order_scooter(Users.NAME[1],
                                 Users.SURNAME[1],
                                 Users.ADDRESS[1],
                                 OrderPageLocators.CHOOSE_SUBWAY2,
                                 Users.PHONE_NUMBER[1],
                                 OrderPageLocators.CHOOSE_DELIVERY_DATE2,
                                 OrderPageLocators.RENT_TIME_CHOOSE2,
                                 OrderPageLocators.COLOUR_OF_SCOOTER_CHOOSE,
                                 Users.COMMENT[1])
        actual_text = order_page.check_success_order()
        assert 'Заказ оформлен' in actual_text
