
def show_phon():
    with open('phon.txt', 'r+', encoding='utf-8') as file:
        book = file.read()
    return book

def new_phon():
    with open('phon.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: '+ '\n') )
    

def find_phon(name):
    with open('phon.txt', 'r+', encoding='utf-8') as file:
        book = file.read().split("\n")
        for i in book:
            if name in i:
                return i

def delete_person(name):
    with open("phon.txt", "r", encoding='utf-8') as f:
        lines = f.readlines()
    with open("phon.txt", "w", encoding='utf-8') as f:
        for line in lines:
            if line.strip("\n") != name:
                f.write(line)

def change_person(new_name, old_name):
    with open("phon.txt", "rt", encoding='utf-8') as f:
        lines = f.readlines()
    with open("phon.txt", "wt", encoding="utf-8") as f:
        for line in lines:
            f.write(line.replace(old_name, new_name))



print("   █████████     ███████       ███████     █████████  ██████████    ███████████   █████  █████████  \n  ███░░░░░███  ███░░░░░███   ███░░░░░███  ███░░░░░███░░███░░░░░█   ░░███░░██████ ░░███  ███░░░░░███ \n ███     ░░░  ███     ░░███ ███     ░░███░███    ░░░  ░███  █ ░     ░███ ░███░███ ░███ ███     ░░░  \n░███         ░███      ░███░███      ░███░░█████████  ░██████       ░███ ░███░░███░███░███          \n░███    █████░███      ░███░███      ░███ ░░░░░░░░███ ░███░░█       ░███ ░███ ░░██████░███          \n░░███  ░░███ ░░███     ███ ░░███     ███  ███    ░███ ░███ ░   █    ░███ ░███  ░░█████░░███     ███ \n ░░█████████  ░░░███████░   ░░░███████░  ░░█████████  ██████████    ██████████  ░░█████░░███████████")

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                  +'0-поиск,\n1-чтение файла,\n2-добавление в файл,\n3-удаление,\n4-замена,\n5-выход\n: ')
    if mode == '1':
        print(show_phon())
    elif mode == '0':
        name = input('что ищем?: ')
        find = find_phon(name)
        print(find)
    elif mode == '2':
        new_phon()
    elif mode == '3':
        name = input('кого удаляем?: ')
        find = find_phon(name)
        delete_person(find)
    elif mode == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        find = find_phon(old_name)
        change_person(new_name,find)
    elif mode == '5':
        break
    else:
        print('No mode')

