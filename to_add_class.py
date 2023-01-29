def add_student():
    dict_student = {}
    dict_student['Name'] = input('Введите имя ученика: ')
    dict_student['Surname'] = input('Введите фамилию ученика: ')
    return dict_student
#Добавление ученика в общий словарь класса с уникальным id
def add_class(dict,id):
    dict[id] = add_student()
    return dict