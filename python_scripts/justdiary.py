from datetime import datetime
import os
def add_entry(text):
    with open('diary.txt', 'a', encoding = 'utf-8') as f:
        today = datetime.now().strftime('[%d.%m.%Y %H:%M]')
        f.write(f'{today}\n{text}\n')
def view_entries():
    if not os.path.exists('diary.txt'):
        print('Дневник пуст')
    else:
        with open('diary.txt', 'r', encoding='utf-8') as f:
            print(f.read())
while True:
    print('1 - Добавить запись\n2 - Посмотреть записи\n0 - Выход')
    if (u := input('Выберите: ')) == '1':
        add_entry(input('Введите запись:\n'))
    elif u == '2':
        view_entries()
    elif u == '0':
        break
    else:
        print('Неверный ввод')
