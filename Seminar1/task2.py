# Проверка истинности утверждения
for x in range(2):
    for y in range(2):
        for z in range(2):
            if not (x or y or z) == ( not x and not y and not z ):
                print(f'Утверждение истинно для x = {x}, y = {y}, z = {z}')
            else:
                print(f'Утверждение не истинно для x = {x}, y = {y}, z = {z}')