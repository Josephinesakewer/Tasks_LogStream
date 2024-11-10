import random
import os
import datetime

def generate_digit():
    x = random.randint(1,100)
    if ( x % 2 == 0):
        print(f'Четное число{x}!')
    else: print((f'Нечетное число{x}!'))
    return x

x = generate_digit()
print(x)

# Создание директории и файла с последующим перемещением
def create_dir():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    base_dir = os.path.join(os.getcwd(), current_date)
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
    
    text_file_path = os.path.join(base_dir, 'task.txt')
    if not os.path.exists(text_file_path):
        with open(text_file_path, 'w') as text_file:
            text_file.write("")

    
    nested_dir = os.path.join(base_dir, 'file_task')
    if not os.path.exists(nested_dir):
        os.mkdir(nested_dir)
    
    
    new_file_path = os.path.join(nested_dir, 'task.txt')
    if not os.path.exists(new_file_path):
        os.rename(text_file_path, new_file_path)
    
    print(f'Файл перемещен в: {new_file_path}')
    print(f'Информация о файле: {os.stat(new_file_path)}')

create_dir()


