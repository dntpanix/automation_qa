some_one_str = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteu sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum
"""
count = 0
for i in some_one_str:
    if i.isupper():
        count = count + 1
        # count += 1
# print(count)

# Списки
## створення списків - пустий і зі значеннями
blank_list = []
big_list = [7, 336, 61, "--==--", 'spam', 'dev', 1.23]
# індексація, зрізи
print(big_list[1])
print(big_list[1:4])
print(big_list[-2])
big_big_list = ["abc", "b", "c", big_list]
print(big_big_list[0][2])
print(big_big_list)


## порівняння списків
a = [1, 3, 2]
b = [1, 3, 2]
c = [1, 3, 2, 4, [1, 3, 2]]
# print(a > b)  # так не робити!!!!
# print(a == b)
# print(a != b)
print(1 in a) # True
print(7 in a) # False
# print(a in b) # not working!!!
print(a in c) # working!!

## методи списків
# додавання у список
big_list.append(4)
big_list.append([4, 5])
print(big_list)
big_list.extend([5, 61, 777])
print(big_list)
big_list.insert(1, "223")
print(big_list)
big_list[1] = int(big_list[1])
print(big_list)
# пошук, перевірка значень
value = 61
print(big_list.index(value))
print(big_list.count(value))
# впорядкування даних
only_str = ['bbc', 'cbc', 'abc']
only_str.sort()  # ['abc', 'ABD', 'aBe']
print(only_str)
big_list.reverse()
print(big_list)

# зміни
new_big = big_list.copy()
print(new_big)

# big_list.clear()
# print(big_list)


# big_list.extend([5,6,7])
# print(big_list)
# big_list.insert(1, "223")
# print(big_list)

## вилучення значень
list_value = big_list.pop(2)
print(list_value)
print(big_list)
# пошук, перевірка значень
# value = 'spam'
# index = big_list.index(value)
# print(index)
# print(big_list.count(7))
# впорядкування даних

small_list =['abc', 'ABD', 'aBe']
number_list = [1,5,4,3,7,2]
small_list.sort()  #
number_list.sort()
print(small_list)
print(number_list)

bl = big_list.copy()

big_list.reverse()
# print(big_list)
# зміни
# print(bl)
# print(big_list)

a = 0.100000000001
b = 0.200000000002
c = 0.300000000003
# print(a)
# print(b)
# print(c)
# comprehensions and List Iteration
int_list = [x**2 for x in range(5)]
print(int_list)

# Словники
## створення словників
blank_dict = {}
small_dict = {'name':'Mary', 'second': 'Ann', 'age': 18}
big_dict= {'user': {'name':'Bob', 'second': 'Hand', 'age': 40},
           'is_blocked': False,
           'salary': 10000}
print(big_dict['user']) ## ['age'] - запит з вкладеного словника
# print("*"*88)
## додавання значень в словник
big_dict['new_key'] = "value"
big_dict.update({"yet_other_key": 12345})
print(big_dict)

## методи словника
for k, v in big_dict.items():
    print(k, v)

print(big_dict.keys())
print(big_dict.values())

# print("*"*88)
new_dict = {}
for key, value in small_dict.items():
    new_dict[value] = key
    #print(k,":", v)
print(new_dict)
# print("*"*88)
print(big_dict["user"]['second'])
# big_dict.copy()
# big_dict.clear()
big_dict["user"] = small_dict
print(big_dict["user"]['second'])
big_dict["is_blocked"] = True
# print(big_dict)
big_dict.update({"user2":{'name':'Bob', 'second': 'Hand', 'age': 40}})
big_dict.update({"page": 12133})
print(big_dict)

value = big_dict.get("page", 32)
print(value)
print(big_dict.pop("page", "default"))  #.popitem() -  видалення випадкового елемента
print(big_dict.pop("page", "default"))
# порівняння словників Dictionary Comparisons
# Example: Word Counts
text = ('this is sample text with several words '
        'this is more sample text with some different words')
# без колекцій
# з колекціями
# from collections import Counter
# from collections import Counter
# c = Counter(text)
# print(c.most_common(5))

text_counter = {} # створили пустий словник
for char in text:    # бере кожну літеру з text і вставляє в змінну char
    if char in text_counter:  # якщо char є в словнику text_counter
        text_counter[char] += 1  # збільшмим на один значення ключа char
    else: # якщо char в словнику немає
        text_counter[char] = 1   # встановимо значення ключа char =1
print(text_counter)

# Zipped key/value tuples form (ahead)
zipped = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print(zipped)

# Сети (набори)
my_blank_set = set()
## перетворення в набір
numbers = list(range(4)) + list(range(10))
print(numbers)
print(set(numbers))
print(set(text))
my_list = [1,2,4,1,4,5,2,7,8,1,3,4,5]
print(set(my_list))

## операції з наборами
# порівняння
# підмножина. Еквівалентом методу issubset() є оператор <=
set_a = {1, 2, 3}
set_b = {1, 2, 4, 5, 3}
print(set_a.issubset(set_b))
print("B <= A", set_b <= set_a)
print("A <= B",set_a <= set_b)
# обєднання  with the '|' operator or with the set type’s 'union' method
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b
union_set = set_a.union(set_b)
print(union_set)

# перетин 'intersection' and with the '&' operator
set_a = {1, 2, 3}
set_b = {3, 4, 5, 1}
intersection_set = set_a & set_b  # {3, 1}
print(intersection_set)
list_set = sorted(intersection_set)
#list_set.sort()
print(list_set)

# симетрична різниця
set_a = {1, 2, 3}
set_b = {3, 4, 5, 1, 2}
symmetric_difference_set = set_b ^ set_a  # {1, 2, 4, 5}
print(symmetric_difference_set)

# кортежі Tuples
student_tuple = ()

# Елементи Tuple можуть бути будь-якого типу, включаючи числа, рядки, списки та інші Tuple. Наприклад:
my_tuple = ("apple", 3.14, [1, 2, 3], (4, 5, 6))
my_tuple[2].insert(3, 4)
# my_tuple[3].insert(3, 4)
print(my_tuple)
my_tuple[2].pop()

# my_tuple[1] += 1  # видасть помилку, оскільки флоат в таплі незмінний!!
# print(my_tuple)
# Для доступу до елементів Tuple можна використовувати індексацію, яка починається з 0. Наприклад:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # "banana"

# Інші корисні операції з Tuple:
# Отримання довжини Tuple:
my_tuple = (1, 2, 3)
# print(len(my_tuple))  # 3

# Злиття двох Tuple:
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = tuple1 + tuple2
print(tuple3)  # (1, 2, 3, "apple", "banana", "cherry")

# Перевірка наявності елемента в Tuple:
my_tuple = (1, 2, 3)
# print(1 in my_tuple)  # True
# print(4 in my_tuple)  # False

# Повторення Tuple:
my_tuple = ("apple", "banana", "cherry")
print(my_tuple * 2)  # ("apple", "banana", "cherry", "apple", ...

print(isinstance(my_tuple, str))
print(isinstance(my_tuple, tuple))