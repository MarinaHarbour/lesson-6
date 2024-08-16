my_dict={'Eva': 2003, 'Sasha': 1999, 'Gleb': 2012 }
print(my_dict)
print(my_dict['Eva'])
print(my_dict.get('Misha'))
my_dict.update({'Alex': 2003,
                'Inna': 1999})
print(my_dict)
abc=my_dict.pop('Gleb')
print(my_dict)
print(abc)

my_set={5,6,5,5,7,8,9,9,'abcd',(1,4,6),'abcd'}
print(my_set)
print(my_set.add(100))
print(my_set.add(101))
print(my_set.discard('abcd'))
print(my_set)