#Формирует словарь где в качестве ключа - школьный предмет
def add_subject(dict, sub):
    subject = {}
    for key,value in dict.items():
        subject[f'{sub}'] = []
        value.update(subject)
        subject.clear()
    return dict