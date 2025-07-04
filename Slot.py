import random

variations = [[1,1,1],[2,2,2],[3,3,3]]
randomnums = []

for _ in range(3):
    randomnums.append(random.randint(1,3))
    
        
if randomnums == variations[0]:
    print(f'{randomnums}\nТы победил с малым каэфом')

elif randomnums == variations[1]:
    print(f'{randomnums}\nТы победил с средним каэфом')

elif randomnums == variations[2]:
    print(f'{randomnums}\nТы победил с высоким каэфом')

else:
    print(f'{randomnums}\nТы проиграл!')