import to_add_class
import to_add_subject
import to_add_grade
import to_list_stud
import gen_report

def contr ():
    dict_class = {}
    subjects = {}
    i = 0
    id = 1
    while i == 0:
        point = int(input('____Меню____\n1-Добавить ученика\n2-Добавить предмет\n3-Поставить оценку\n4-Список учеников\n5-Успеваемость ученика\n6-Выйти и сформировать отчет\n'))
        if point == 1:
            dict_class = to_add_class.add_class(dict_class,id)
            id+=1
        elif point == 2:
            dict_class = to_add_subject.add_subject(dict_class, input('Введите название предмета: '))
        elif point == 3:
            dict_class = to_add_grade.add_grade(dict_class,input('id ученика: '),input('Предмет: '), int(input('Оценка: ')))
        elif point == 4:
            to_list_stud.list_stud(dict_class)
        elif point == 5:
            print(dict_class[int(input('id ученика: '))][input('Предмет: ')])
        elif point == 6:
            gen_report.gen_raport(dict_class) 
            i = 1
    