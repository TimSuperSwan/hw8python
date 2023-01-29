def list_stud(dict):
    for key,value in dict.items():
        print(key, value['Name'], value['Surname'])

# dict = {1:{'name': 'artem', 'surname': 'lebedev'},2:{'name': 'bogdan', 'surname': 'nidenov'}}
# list_stud(dict)