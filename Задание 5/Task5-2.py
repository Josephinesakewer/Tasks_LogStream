import random
import calendar
import re 

def accept_list():
    list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]
    x = random.choices(list_el)
    y = random.choices(list_el)
    return x,y

print(accept_list())


def data_format(date_str):
    if re.match(r'^\d{4}-(0[1-9]|1[0-2])$', date_str):
        year, month = map(int, date_str.split('-'))
        # Печать календаря на заданный месяц и год
        print(calendar.month(year, month))
    else:
        print("Неверный формат даты! Введите дату в формате ГГГГ-ММ.")

# Пример использования
data_format("2024-11")  # Корректный формат
data_format("2024-13")  # Неверный формат месяца
data_format("24-11")    # Неверный формат года


# Регулярное выражение для проверки российского номера телефона
phone_pattern = r'^(?:\+7|7|8)\d{10}$'

# Функция для проверки номера телефона
def num_phone(phone_number):
    if re.match(phone_pattern, phone_number):
        print("Корректный номер телефона")
    else:
        print("Некорректный номер телефона")

num_phone("+71234567890")  
num_phone("81234567890")  
num_phone("71234567890")   
num_phone("1234567890")    
num_phone("+723456789012")