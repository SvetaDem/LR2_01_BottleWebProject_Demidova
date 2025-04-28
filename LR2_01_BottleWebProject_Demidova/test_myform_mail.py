import unittest
from myform_mail import is_valid_email

class TestEmailValidation(unittest.TestCase):
    
    def test_invalid_emails(self):
        list_mail_uncor = [
            "", "1", "m1@", "@mail", "mail@", "m1@.com", 
            "m1@mail", "m1@com", "m1@.com.", "m1@mail..com",
            "m1@@mail.com", "m mail@mail.com", "m1@mail .com", 
            "m1@mail,com", "_m@mail.com", "m..m@mail.com", "mm@mail.r"
        ]
        for email in list_mail_uncor:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email), f"Должен быть невалидный: {email}")
    
    def test_valid_emails(self):
        list_mail_cor = [
            "m.m@mail.ru", "m1@gmail.com", "my-email123@example.com", 
            "1email@example.com", "user_name@example.net"
        ]
        for email in list_mail_cor:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email), f"Должен быть валидный: {email}")

if __name__ == "__main__":
    unittest.main()
