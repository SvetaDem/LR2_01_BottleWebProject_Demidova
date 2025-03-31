from bottle import post, request
import re
from datetime import datetime

@post('/home')
def my_form():
    username = request.forms.get('USERNAME').strip()
    email_address = request.forms.get('ADRESS').strip()
    question = request.forms.get('QUEST').strip()

    # Проверка заполненности полей
    if not username or not email_address or not question:
        return "All fields are required. Please fill out the form."

    # Проверка формата email
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z]{2,}$'
    if not re.fullmatch(email_pattern, email_address):
        return "Invalid email format. Please enter a valid email."

    # Получение текущей даты
    current_date = datetime.now().strftime("%Y-%m-%d")

    return "Thanks, {}! The answer will be sent to {}. Access Date: {}".format(username, email_address, current_date)

