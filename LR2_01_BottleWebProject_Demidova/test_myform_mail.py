import unittest
from myform_mail import is_valid_email

class TestEmailValidation(unittest.TestCase):
    
    def test_invalid_emails(self):
        list_mail_uncor = [
            "", # пустая строка
            "1", # нет символа @
            "m1@", # нет домена
            "@mail", # нет имени пользователя
            "m1@.com", # домен начинается с точки
            "m1@mail", # нет доменной зоны (.com, .ru)
            "m1@com", # нет точки в домене
            "m1@.com.", # начинается и заканчивается точкой
            "m1@mail..com", # две точки подряд в домене
            "m1@@mail.com", # двойной символ @
            "m..m@mail.com", # две точки подряд в имени
            "m mail@mail.com", # пробел в имени
            "m1@mail .com", # пробел в домене
            "m1@mail,com", # запятая вместо точки
            "_m@mail.com", # начинается со спец-символа
            "mm@mail.r", # доменная зона < 2 символов
            "m@mail.com", # имя < 2 символов
            "m"*65+"@mail.com", # имя > 64 символов
            "mm1@m."+"m"*254, # общая длина домена > 255 символов
            "m\\@mail.com", # недопустимые символы в имени
            "mm@mail.r-u" # недопустимые символы в домене
        ]
        for email in list_mail_uncor:
            self.assertFalse(is_valid_email(email), f"Должен быть невалидный: {email}")
    
    def test_valid_emails(self):
        list_mail_cor = [
            "m.m@mail.ru", # имя с точкой, стандартный домен
            "m1@gmail.com", # имя с цифрой, стандартный домен
            "my-email123@example.com", # имя с дефисом и цифрами
            "1email@example.com", # начинается с цифры
            "user_name@example.net", # имя с подчёркиванием
            "a"*64+"@mail.com", # имя из 64 символов — максимальная допустимая длина
            "user@" + "d"*251+".com" # доменная часть ~250 символов (общая длина <= 255)
        ]
        for email in list_mail_cor:
            self.assertTrue(is_valid_email(email), f"Должен быть валидный: {email}")

if __name__ == "__main__":
    unittest.main()
