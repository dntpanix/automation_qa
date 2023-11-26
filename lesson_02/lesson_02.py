# Логічна лінія та фізична лінія
print("Task 10:")
book_1 = 8
book_2 = book_1 + 2
book_3 = int((book_1 + book_2)/2)
total_book = book_1 + book_2 + book_3
print(f"Так, як перша книжка коштує {book_1}, друга - на 2 грн. дороже" \
    "- то нам потрібно 8 грн додати 2 грн - то це означає, що друга книга" \
    f"довірнює {book_2}, а третя - як половина вартості першої та другої разом" \
    f"- то нам потрібно добавити {book_1} грн та {book_2} грн і поділити на два," \
    f"і тоді третя книжка дорівнює {book_3} грн, всі книжки разом будуть коштувати {total_book} грн")


first_line = """<tr><td><a href='https://link.company.com/screens/drqs{drqs_number}' target='_blank'>
    {drqs_number}</a></td><td>{routeToGroup}</td><td>{createdDate}</td><td>{owner}</td>
    <td>{status}</td><td>{last_update}</td><td>{author}</td><td>{skipped_tests}</td>
    <td>{scope}</td></tr>"""
# print(first_line)

second_line = ("asdfghjklqwertyu"
    "1234567890"
    ")(*&^%#%#&*&^%??><<@!)"
    "djfhdjd,f")
# print(second_line)
# Оператори дій
1+1
1-2
1*1
# +  -  *  /  %   **  //  <<  >>  &   @
# |  ^  ~  <  <=  >   >=  !=  ==  @=  :=

# Розділювачі та Спеціальні токени
"""
(    )    [    ]    {    }

,    :    .    =    ;    @

+=   -=   *=   /=   //=  %=

&=   |=   ^=   >>=  <<=  **=
"""
#  '  "  \

# Літерали
42
"hello"
"""get me
more Python"""
1.23

# Типи даних
## Цілі числа
aples = 5
users = 2
count_aples = aples / users
# print(count_aples)

## Строки
hello = "hello"
word = 'word'
english_words = 'I don\'t know'
# print(english_words)
## Кортежі (Tuples)
(0, 2, 4, 6)
## Списки [Lists]
new_list = ["a", 0, 1.2, hello]
# print(new_list)
## Набори {Sets}
simple_set = { 1, 2, 3, 1}
# print(simple_set)
## Словники {Dictionaries: 2}
samle_dict = {"key": "value"}
## None
a = None
## Булеві значення
True
False
1 == 1
2 > 56
# "a" < 45  # різні типи - помилка!!!
# Змінні у Пітоні
storona_1 = 1
storona_2 = 1 + 1
_some_var_ = 2

# Об’єкти у Пітоні
class SampleObj():
    a = 1
    def some_def(self):
        print("YAHHHHHHHHHHOOOOOOOOOOOOOOOOOO")
yet_other_obj = SampleObj()
## Атрибути об’єкта
# print(yet_other_obj.a)
## Елементи об’єкта
# print(samle_dict["key"])
## Методи -  виклик операції з об’єктом
# yet_other_obj.some_def()
# Числові операції
## Ділення
s = 22 / 7
# print(s)
s2 = 22 // 7
# print(s2)
s3 = 22 % 7
# print(s3)
s4 = 22 - (7 * s2)
# print(s4 == s3)
## Множення, додавання, віднімання
x = 2
x2 = x * 2
# print(x2)
# print("*" * 8)
# print("sa"+"sha")


## Піднесення у степінь
# print (2**8)
## Порівняння
(1 < 2) and (2 < 3)
(2 < 1) or (2 < 3)
# Ввод та вивід даних
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
## f-string
year = 2006
event = 'referendum'
msg = f'Results of the {year} {event.capitalize()}'
# print(msg)
## format
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
# print("{1:10d} YES votes \n{0:10d} NO".format(yes_votes, no_votes))

for x in range(1, 11):
    pass
    # print('{0:2d} {1:4d} {2:6d}'.format(x, x*x, x*x*x))

## concatenate
f_list = ["aple", "banana", "kivi"]
fruits = ", ".join(f_list)
# print(fruits)

## multiply

## ввод
# eggs = input("Скількі яєць на сніданок бажаєте? ")
# eggs = int(eggs)
# print(f"Ви замовили {eggs*2} яєць (ваш бонус враховано)")
