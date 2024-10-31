my_dict = {'Aleksey' : 1998 , 'Olga' : 1989, 'Maksim' : 1990, 'Pavel' : 1995}
print(my_dict)
print(my_dict['Maksim'])
print(my_dict.get('Irina'))
my_dict.update({'Aleksandr' : 1985,
                'Mariya' : 1993 })
print(my_dict)
print('delete value:' , my_dict['Olga'])
del my_dict['Olga']
print(my_dict)

my_set = {1,2,3,3,2,4, 'string' , 12.33, False}
print(my_set)
my_set.add(5)
my_set.add('My string')
my_set.remove(False)
print(my_set)

