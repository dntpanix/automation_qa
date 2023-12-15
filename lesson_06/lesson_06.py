from collections import Counter
# Булеві значення та порівняння
car = 'bmw'
print(car == 'bmw')
print(car == 'audi')

False # "", {}, [], (), 0

olya = 0
age = 44
if age <= 18:  # if age <= 18 or name[0] == "A":
    olya = 3.1415
    print("You are too young!")
elif age >= 25:
    pass
elif age >= 35:
    olya = 7.3465
    pass
elif age >= 45:
    print("You are too old")


if olya:
    print("ok")

# else:
#     print("Ok, and you have a discount")
age =  18 # int(input("Type your age: "))

message = "Please try again!" if age < 18 else "Ok, can go!"
print(message)

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото.
Який альбом треба виготовти для вклейки фото?
"""

BOOKLET = 8

total_photo = 65 # 232 # int(input("К-сть фото: "))
photo_per_page = 8 # int(input("К-сть фото на  1 сторінку: "))

est_page = total_photo // photo_per_page
rest_page = total_photo % photo_per_page
if (est_page % BOOKLET) > 0:
    add_page = BOOKLET - est_page % BOOKLET
    est_page = est_page + add_page
elif rest_page > 0:
    est_page = est_page + BOOKLET
print(est_page, rest_page)

current_number = 0
while current_number <= 4:
    current_number += 1
    if current_number == 4:
        # break  # прервати
        continue # пропустити
    print("while print me:", current_number)

for i in range(1, 5):
    print(i)

for i in range(10, 5, -1):
    print(i)
print("*"*88)
my_list = [7, 2, 4, 4, 5, 6, 3, 8]
for i in my_list:
    print(i)

# new_list= []
# for i in my_list:
#     if i % 2:
#         continue
#     else:
#         new_list.append(i)

# print(new_list)

new_list = [i for i in my_list if i % 2 == 0]
print(new_list)

dict_01 = {'а': 2, 'б': 3, 'в': 1}
dict_02 = {'б': 3, 'в': 1, 'а': 2}
dict_03 = {'а': 45, 'б': 3, 'u': 11}
print(dict_01 == dict_03)

def dict_compare(d1, d2):
    cnt1 = Counter(d1)
    cnt2 = Counter(d2)
    return cnt1 == cnt2

print(dict_compare(dict_01, dict_03))

print(dict_01.keys() == dict_03.keys())
print(set(dict_01.keys()) ^ set(dict_03.keys()))
print(dict_01.values() == dict_03.values())
print(set(dict_01.values()) ^ set(dict_03.values()))