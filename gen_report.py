dict_class = {1:{'Name': 'artem', 'Surname': 'lebedev', 'Physic': [5,4,3]}, 2:{'Name': 'bogdan', 'Surname': 'nidenov','Physic': [4]}}
def gen_raport(dict):
    with open('report.txt','w') as file:
        for key,value in dict.items():
            for i,val in value.items():
                if type(val) == list:
                    a = ','.join(str(x) for x in val)
                    file.write(f'{i}: {a} ')
                else:
                    file.write(f'{i}: {val} ')
            file.write('\n')
gen_raport(dict_class)    

