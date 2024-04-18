Спринт 5
Проект автоматизации тестирования конструктора космического фастфуда

Основа для написания автотестов — фреймворк pytest.

Содержимое проекта
Директория проекта:

test_build_in_general.py - Проверка работы конструктора с разделами "Булки", "Соусы", "Начинки"
test_exit_from_account.py - Проверка кнопки выхода из личного кабинета
test_general_page_login_button.py - Проверка входа в аккаунт разными способами
test_login_page_correct_password.py - Проверка регистрации аккаунта при вводе пароля больше или равным шести символам
test_login_page_not_correct_password.py - Проверка вывода ошибки при вводе пароля короче шести символов
test_transition_to_builder_and_logo.py - Проверка перехода в конструктор и по клику на Лого из личного кабинета
test_transition_to_personal_account.py - Проверка возможности входа в личный кабинет

random_mail.py - генератор рандомных email
locators.py - локаторы
conftest.py - фикстуры