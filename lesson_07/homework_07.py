# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_numbers(a, b):
    result = a + b
    return result
print(sum_numbers(2,3))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

number_list = [2, 4, 6, 8, 10]
average_result = calculate_average(number_list)
print(f"The average of the numbers is: {average_result}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string
original_string = "Hello, Hillel!"
result = reverse_string(original_string)
print(f"The original string: {original_string}")
print(f"The reversed string: {result}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def long_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word
words = ["apple", "banana", "kiwi", "strawberry", "orange"]
result = long_word(words)
print(f"The list of words: {words}")
print(f"The longest word: {result}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return -1

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

'''мій варіант'''
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
result = find_substring(str1, str2)
print(f"The index of the substring '{str2}' in '{str1}': {result}")

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
result = find_substring(str1, str2)
print(f"The index of the substring '{str2}' in '{str1}': {result}")

# task 7
def calculate_bananas(apples):
    banana = apples * 4
    return banana

apples = 5
result = calculate_bananas(apples)
print(result)

# task 8
def calculate_total_trees(apple_tree):
    pearl_tree = apple_tree + 5
    plump_tree = apple_tree - 2
    total_trees = apple_tree + pearl_tree + plump_tree
    return total_trees

apple_tree = 3
result = calculate_total_trees(apple_tree)
print(result)

# task 9
def calculate_temperatures(morning_temperature):
    day_temperature = morning_temperature - 10
    evening_temperature = day_temperature + 4
    return morning_temperature, day_temperature, evening_temperature

morning_temperature = 5
result = calculate_temperatures(morning_temperature)
print(result)

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
def calculate_total_cost_books(cost_book_1):
    cost_book_2 = cost_book_1 + 2
    cost_book_3 = (cost_book_1 + cost_book_2) / 2
    total_cost_books = cost_book_1 + cost_book_2 + cost_book_3
    return total_cost_books

cost_book_1 = 8
result = calculate_total_cost_books(cost_book_1)
print(result)