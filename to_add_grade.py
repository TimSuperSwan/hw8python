def add_grade(dict,id,subj,grade):
    a = dict[int(id)][subj]
    dict[int(id)][subj].append(grade)
    return dict

# dict = {1:{'name': 'artem', 'surname': 'lebedev', 'physic': [0]},2:{'name': 'bogdan', 'surname': 'nidenov'},'physic': [1, 2, 3]}

# add_grade(dict,1,'physic', 4)
# add_grade(dict,'1','physic',9999)
# print(dict)


