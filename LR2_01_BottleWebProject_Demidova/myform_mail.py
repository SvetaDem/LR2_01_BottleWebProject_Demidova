import re

# Регулярное выражение для проверки email
email_pattern = r"^(?=[a-zA-Z0-9])(?!.*\.\.)[a-zA-Z0-9_.-]{2,64}@(?=.{1,255}$)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

# Функция проверки email
def is_valid_email(email_address: str) -> bool:
    return bool(re.fullmatch(email_pattern, email_address))

