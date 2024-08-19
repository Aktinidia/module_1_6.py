my_dict = {'Nataliya': 1977, 'Sergey': 1978, 'Viktor': 1926, 'Irina': 1980}
print('Словарь: ', my_dict)
print('Существующее значение: ', my_dict['Nataliya'])
print('Несуществующее значение: ', my_dict.get('Denis'))
my_dict.update({'Anna': 1985, 'Alexandr': 1988})
print('Удалённое значение: ', my_dict.pop('Viktor'))
print('Измененный словарь: ', my_dict)
my_set = {10, 2.5, True, 'Мышь', 2.5, 10, 'Мышь', True}
print('Множество: ', my_set)
my_set.add('Кот')
my_set.add('Пёс')
my_set.remove(True)
print('Измененное множество: ', my_set)