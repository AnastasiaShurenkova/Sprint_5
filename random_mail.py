import random
import string


def generate_email():
    # Генерируем случайную строку для имени email
    letters = string.ascii_letters
    email_name = ''.join(random.choice(letters) for i in range(10))

    # Генерируем случайный домен email
    domains = ['ya.ru', 'gmail.com', 'mail.ru', 'rambler.com']
    email_domain = random.choice(domains)

    # Объединение имени и домена
    email = email_name + '@' + email_domain

    return email


random_email = generate_email()