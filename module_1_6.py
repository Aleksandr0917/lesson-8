my_dict={'Alex':1973, 'Bob':2002, 'Andrey':1987 }
print(my_dict)
print(my_dict.get('Bob'))
print(my_dict.get('Rob'))
my_dict.update({'Zakhar':2013,
                'Ivan':2013})
print(my_dict)
del my_dict ['Bob']
print(my_dict)

my_set={1, 2, 3, 1, 1, 4, 5, 4, 'wind',(1, 2, 3)}
print(my_set)
my_set.update({41,'apple'})
print(my_set.remove(2))