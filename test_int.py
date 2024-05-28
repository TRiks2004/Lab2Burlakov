import unittest
from myform import проверка_email, проверка_имя
from bottle import HTTPError

class TestFormValidation(unittest.TestCase):

    def test_invalid_emails(self):
        """
        Проверка неверных email адресов.
        """
        invalid_emails = [
            "",                     # Пустая строка
            "1",                    # Неверный формат (отсутствие символа @)
            "m1@",                  # Неверный формат (отсутствие доменной части)
            "@mail",                # Неверный формат (отсутствие имени пользователя)
            "user@mail",            # Неверный формат (отсутствие доменной части)
            "user@mail.",           # Неверный формат (отсутствие доменной части)
            "user@mail.com.",       # Неверный формат (точка в конце доменной части)
            "user@.com",            # Неверный формат (отсутствие имени пользователя)
            "user@com",             # Неверный формат (отсутствие точки в доменной части)
            "user.com",             # Неверный формат (отсутствие символа @)
            "user@.com.",           # Неверный формат (две точки подряд после @)
            "user@domain.com.",     # Неверный формат (точка в конце адреса)
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                with self.assertRaises(HTTPError):
                    проверка_email(email)

    def test_valid_emails(self):
        """
        Проверка корректных email адресов.
        """
        valid_emails = [
            "mm@mail.ru",
            "m1@gmail.com",
            "user123@example.com",
            "name@example.com",
            "user@subdomain.example.com",
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                    проверка_email(email)


    def test_invalid_names(self):
        """
        Проверка неверных имен.
        """
        invalid_names = [
            "",             # Пустая строка
            " ",            # Строка только из пробелов
            "us",           # Слишком короткое имя
            "user name",    # Присутствие пробелов
            "user@",        # Присутствие символа '@'
            "user_name_longer_than_twenty_characters"  # Длина больше 20 символов
        ]
        for name in invalid_names:
            with self.subTest(name=name):
                with self.assertRaises(HTTPError):
                    проверка_имя(name)

    def test_valid_names(self):
        """
        Проверка корректных имен.
        """
        valid_names = [
            "username",
            "user123",
            "name_lastname",
            "user_name_123",
            "valid_name",
            "another_name",
        ]
        for name in valid_names:
            with self.subTest(name=name):
                try:
                    проверка_имя(name)
                except HTTPError:
                    self.fail(f"проверка_имя('{name}') raised HTTPError unexpectedly!")

if __name__ == '__main__':
    unittest.main()
