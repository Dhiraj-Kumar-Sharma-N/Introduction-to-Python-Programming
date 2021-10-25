# ================================ LOOPS  =================================

# ================================ FOR LOOPS  =================================

# Basic loop for List
List_Items = [1, 6, 8, 'Dhiraj']

for each_item in List_Items:
    print(each_item)

for each_item in [1, 6, 8, 'Dhiraj']:
    print(each_item)

# Basic loop for String

for each_char in 'Dhiraj':
    print(each_char)

index = 0
for each_char in 'python':
    print(f'{each_char} --> {index}')
    index = index + 1

# List in List
for x, y in [[1, 6], [8, 6]]:
    print(f'x = {x},y = {y}')
    # x = 1,y = 6
    # x = 8,y = 6

# Tuple in List
for x, y, z in [(1, 6, 'Dhiraj'), (8, 6, 'Kumar')]:
    print(f'x = {x},y = {y},,z = {z}')
    # x = 1,y = 6,,z = Dhiraj
    # x = 8,y = 6,,z = Kumar

# loop for Dictionary
Dictionary_items = {1: 'One', 2: 'Two', 3: 'Three'}
for Key, Value in Dictionary_items.items():
    print(Key)
    print(Value)

Dictionary_items = {1: 'One', 2: 'Two', 3: 'Three'}
for Dic_Obj in Dictionary_items.keys():
    print(Dic_Obj)

Dictionary_items = {1: 'One', 2: 'Two', 3: 'Three'}
for Dic_Obj in Dictionary_items.values():
    print(Dic_Obj)

# ================================WHILE LOOPS  =================================

Count = 1
while Count <= 4:
    print(Count)
    Count = Count + 1

for each in range(1, 11):
    if each == 7:
        break
    print(each)

Count = 1
while True:
    print(Count)
    Count = Count + 1
    if Count == 100:
        break

for each in range(1, 11):
    if each == 7:
        continue
        print("nothing gets executed after Continue in FOR loop")
    print(each)
