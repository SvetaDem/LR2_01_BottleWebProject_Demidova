from bottle import post, request
import re
from datetime import datetime
import pdb
import json
import os

path = 'C:\\Users\\Светлана\\Desktop\\learning\\МДК\\МДК 02.02 Инструментальные средства разработки ПО, У.С. Опалева\\Programs\\LR2_01_BottleWebProject_Demidova\\data.json'

# Функция для загрузки данных из файла
def load_json():
    if os.path.exists(path):
        try:
            file = open(path, 'r')
            data = json.load(file)
            file.close()
        except:
            data = {}
    return data

# Функция для сохранения данных в файл
def save_json(data):
    file = open(path, 'w')
    json.dump(data, file, indent=4)
    file.close()

@post('/home')
def my_form():
    username = request.forms.get('USERNAME').strip()
    email_address = request.forms.get('ADRESS').strip()
    question = request.forms.get('QUEST').strip()

    # Проверка заполненности полей
    if not username or not email_address or not question:
        return "All fields are required. Please fill out the form."

    # Проверка формата email
    email_pattern = r"^(?!\.)(?!.*\.\.)[a-zA-Z0-9_.-]{2,64}@(?=.{1,255}$)[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"

    if not re.fullmatch(email_pattern, email_address):
        return "Invalid email format. Please enter a valid email."

    # Проверка вопроса (длина > 3 символов и не только цифры)
    if len(question) <= 3 or question.isdigit():
        return "Question must be more than 3 characters and not just numbers."

    # Получение текущей даты
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Загрузка существующих данных
    data = load_json()

    # Проверяем, есть ли email в JSON
    if email_address not in data:
        data[email_address] = {
            "username": username,
            "questions": []
        }

    # Проверяем, есть ли такой вопрос уже в списке
    if question not in data[email_address]["questions"]:
        data[email_address]["questions"].append(question)
        save_json(data)  # Записываем обновленные данные
        return "Thanks, {}! The answer will be sent to {}. Access Date: {}".format(username, email_address, current_date)
    else:
        return "Duplicate question detected. It will not be saved."


# --------------Задание №5-------------
# Теперь формируем `questions_dict`
# questions_dict = {email_address: data[email_address]}

# --------------Задание №6-------------
# Запись в словарь (email – ключ, question – значение)
# questions_dict = {email_address:[username,question]}
# pdb.set_trace()

    