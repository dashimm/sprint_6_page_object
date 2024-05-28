import allure
from pages.base_page import BasePage
from locators.home_page_locators import HeaderLocators
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Клик на кнопку Заказать в хэдере')
    def click_on_order_but_from_header(self):
        self.click_to_element(HeaderLocators.ORDER_BUT_HEADER)

    @allure.step('Клик на кнопку Заказать внизу страницы')
    def click_on_order_but_from_under(self):
        self.scroll_to_element(HeaderLocators.ORDER_BUT_UNDER)
        self.click_to_element(HeaderLocators.ORDER_BUT_UNDER)

    @allure.step('Заполняем поле "Имя"')
    def set_name_to_field(self, name):
        self.set_text_to_field(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_surname_to_field(self, surname):
        self.set_text_to_field(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('Заполняем поле "Адрес"')
    def set_address_to_field(self, address):
        self.set_text_to_field(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Выбираем станцию метро')
    def set_subway_station(self, station):
        self.click_to_element(OrderPageLocators.SUBWAY_FIELD)
        self.click_to_element(station)

    @allure.step('Заполняем поле "Телефон"')
    def set_phone_number(self, phone_number):
        self.set_text_to_field(OrderPageLocators.PHONE_NUMBER_FIELD, phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбираем дату доставки')
    def set_date(self, delivery_date):
        self.click_to_element(OrderPageLocators.DELIVERY_DATE_FIELD)
        self.click_to_element(delivery_date)

    @allure.step('Выбираем срок аренды')
    def set_rent_time(self, rent_time):
        self.click_to_element(OrderPageLocators.RENT_TIME_FIELD)
        self.click_to_element(rent_time)

    @allure.step('Выбираем цвет самоката')
    def set_color(self, color):
        self.click_to_element(color)

    @allure.step('Заполняем поле "Комментарии"')
    def set_comment(self, comment):
        self.set_text_to_field(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step('Появление всплывающего окна "Заказ оформлен"')
    def check_success_order(self):
        return self.wait_for_visibility_of_element(OrderPageLocators.ORDER_POPUP_WINDOW).text

    def order_scooter(self, name, surname, address, subway_station, phone_number, delivery_date, rent_time, color, comment):
        self.set_name_to_field(name)
        self.set_surname_to_field(surname)
        self.set_address_to_field(address)
        self.set_subway_station(subway_station)
        self.set_phone_number(phone_number)
        self.click_to_next_button()
        self.set_date(delivery_date)
        self.set_rent_time(rent_time)
        self.set_color(color)
        self.set_comment(comment)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.click_to_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
