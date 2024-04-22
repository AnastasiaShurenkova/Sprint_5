from selenium.webdriver.common.by import By


class StellarBurgers:

    NAME_SELECTOR = (By.XPATH, ".//label[text() = 'Имя']/following-sibling::input") # Поле ввода имени в фоме регистрации
    EMAIL_SELECTOR = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input") # Поле ввода email в форме регистрации
    PASSWORD_SELECTOR = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля в форме регистрации
    REGISTRATION_BUTTON = (By.XPATH, ".//button[text() = 'Зарегистрироваться']") # Кнопка "Зарегистрироваться" в форме регистрации
    PASSWORD_ERROR = (By.XPATH, ".//p[text() = 'Некорректный пароль']") # Всплывающая ошибка в форме регистрации при вводе пароля короче шести символов
    LOGIN_BUTTON_IN_GENERAL = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") # Кнопка "Войти в аккаунт" на главной странице
    EMAIL_AUTHORIZATION_SELECTOR = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and  @name = 'name']") # Поле ввода email в форме авторизации на сайте
    PASSWORD_AUTHORIZATION_SELECTOR = (By.XPATH, ".//input[@name = 'Пароль']") # Поле ввода пароля в форме авторизации на сайте
    AUTHORIZATION_BUTTON = (By.XPATH, ".//button[text() = 'Войти']") # Кнопка "Войти" на странице авторизации на сайте
    CABINET_BUTTON_IN_GENERAL = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка "Личный Кабинет" в правом верхнем углу сайта
    LOGIN_IN_REGISTRATION_WINDOW = (By.XPATH, ".//a[@class = 'Auth_link__1fOlj']") # Кнопка "Войти" на странице с формой регистрации
    NEW_PASSWORD = (By.XPATH, ".//a[text() = 'Восстановить пароль']") # Кнопка "Восстановить пароль"
    BUILDER_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']") # Кнопка "Конструктор" в левом верхнем углу сайта
    LOGO = (By.XPATH, './/div[@class = "AppHeader_header__logo__2D0X2"]') # Логотип по центру вверху сайти
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']") # Кнопка "Выйти" в личном кабинете
    ROLLS = (By.XPATH, ".//span[text() = 'Булки']") # Вкладка "Булки"
    ROLLS_SECTION = (By.XPATH, ".//span[text() = 'Булки']/parent::div") # Поле "Булки"
    SAUCES = (By.XPATH, ".//span[text() = 'Соусы']") # Вкладка "Соусы"
    SAUCES_SECTION = (By.XPATH, ".//span[text() = 'Соусы']/parent::div") # Поле "Соусы"
    FILLINGS = (By.XPATH, ".//span[text() = 'Начинки']") # Вкладка "Начинки"
    FILLINGS_SECTION = (By.XPATH, ".//span[text() = 'Начинки']/parent::div") # Поле "Начинки"
    BUTTON_CHECKOUT = (By.XPATH, ".//button[text() = 'Оформить заказ']") # Кнопка "Оформить заказ"
    ACCOUNT_TEXT = (By.XPATH, ".//p[text() = 'В этом разделе вы можете изменить свои персональные данные']")

