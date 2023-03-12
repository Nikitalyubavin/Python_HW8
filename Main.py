# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска
#    определенной записи (например, имя или фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.

# Русанова Александра Тимофеевна 3-43-15
# Новикова Дарья Гордеевна 2-42-52
# Олейникова Ирина Матвеевна 2-43-50
# Зорина Ева Леонидовна 2-40-20
# Смирнов Денис Денисович 2-39-02
# Поляков Леонид Алиевич 2-35-92
# Соколова Василиса Александровна 3-48-23
# Бородин Максим Адамович 3-78-20
# Гусева Алина Макаровна 2-58-46

def searchInformation(input):
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        temp = file.readlines()
        count = 0
        for line in temp:
            if (str(input).lower() in str(line).lower()):
                print(line)
            else: count += 1
        if (count == len(temp)):
            print('Данные не найдены!')
            print()
    menu()

def showInformation(file):
    line = file.read()
    print(line)
    file.close()
    menu()

def addInformation():
    with open('phonebook.txt', 'a', encoding='utf8') as work_data:
        surname = input('Фамилия: ')
        name = input('Имя: ')
        fatherName = input('Отчество: ')
        phone = input('Телефон: ')
        work_data.write(f'{surname} {name} {fatherName} {phone}\n')
    menu()

def deleteInformation(Input):
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        temp = file.readlines()
    with open('phonebook.txt', 'w', encoding='utf8') as file:
        count = 0
        for line in temp:
            if (str(Input).lower() in str(line).lower()):
                print(line)
                print('Строка удалена!\n')
                temp.remove(line)
                result = "".join(temp)
                file.write(result)
                break
            else: count += 1
        if (count == len(temp)):
            print('Данные не найдены!')
            print()
    menu()

def editInformation(Input):
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        temp = file.readlines()
    with open('phonebook.txt', 'w', encoding='utf8') as file:
        count = 0
        for line in temp:
            if (str(Input).lower() in str(line).lower()):
                print(line)
                temp.remove(line)
                surname = input('Фамилия: ')
                name = input('Имя: ')
                fatherName = input('Отчество: ')
                phone = input('Телефон: ')
                line = (f'{surname} {name} {fatherName} {phone}\n')
                temp.insert(count, line)
                result = "".join(temp)
                file.write(result)
                break
            else: count += 1
        if (count == len(temp)):
            print('Данные не найдены!')
            print()
    menu()


def menu():
    print("Для работы со справочником используйте следующее меню.")
    print('1 - сам справочник, 2 - поиск, 3 - добавление, 4 - удаление, 5 - редактирование')
    print('Для завершения работы нажмите любую другую цифру!')
    num = int(input('Выбор: '))
    if num == 1: showInformation(open('phonebook.txt', 'r', encoding='utf8'))
    elif num == 2: searchInformation(input('Введите параметр поиска: ')) 
    elif num == 3: addInformation()
    elif num == 4: deleteInformation(input('Введите параметр поиска: '))
    elif num == 5: editInformation(input('Введите параметр поиска: '))

menu()