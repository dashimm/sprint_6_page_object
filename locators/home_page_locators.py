from selenium.webdriver.common.by import By


class HeaderLocators:
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    ORDER_BUT_HEADER = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUT_UNDER = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")


class HomePageLocators:
    COOKIE_BUT = (By.ID, 'rcc-confirm-button')
    FAQ_LIST = (By.CSS_SELECTOR, '.accordion')
    QUESTIONS_LIST = [(By.ID, 'accordion__heading-0'),
                      (By.ID, 'accordion__heading-1'),
                      (By.ID, 'accordion__heading-2'),
                      (By.ID, 'accordion__heading-3'),
                      (By.ID, 'accordion__heading-4'),
                      (By.ID, 'accordion__heading-5'),
                      (By.ID, 'accordion__heading-6'),
                      (By.ID, 'accordion__heading-7')]

    ANSWERS_LIST = [(By.ID, 'accordion__panel-0'),
                    (By.ID, 'accordion__panel-1'),
                    (By.ID, 'accordion__panel-2'),
                    (By.ID, 'accordion__panel-3'),
                    (By.ID, 'accordion__panel-4'),
                    (By.ID, 'accordion__panel-5'),
                    (By.ID, 'accordion__panel-6'),
                    (By.ID, 'accordion__panel-7')]
