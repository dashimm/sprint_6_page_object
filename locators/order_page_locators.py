from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = [By.XPATH, "//input[@placeholder = '* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder = '* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"]
    SUBWAY_FIELD = [By.CLASS_NAME, 'select-search__value']
    CHOOSE_SUBWAY1 = [By.XPATH, ".//div[text() = 'Парк культуры']"]
    CHOOSE_SUBWAY2 = [By.XPATH, ".//div[text() = 'Черкизовская']"]
    PHONE_NUMBER_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    DELIVERY_DATE_FIELD = [By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"]
    CHOOSE_DELIVERY_DATE1 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--022']"
    CHOOSE_DELIVERY_DATE2 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--023']"
    RENT_TIME_FIELD = [By.CLASS_NAME, 'Dropdown-control']
    RENT_TIME_CHOOSE1 = [By.XPATH, ".//div[text() = 'двое суток']"]
    RENT_TIME_CHOOSE2 = [By.XPATH, ".//div[text() = 'пятеро суток']"]
    COLOUR_OF_SCOOTER_CHOOSE = [By.ID, 'black']
    COMMENT_FIELD = [By.XPATH, "//input[@placeholder = 'Комментарий для курьера']"]
    BACK_BUTTON = [By.XPATH, ".//button[text() = 'Назад'"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    CONFIRM_ORDER_BUTTON = [By.XPATH, ".//button[text() = 'Да']"]
    ORDER_POPUP_WINDOW = [By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]"]
