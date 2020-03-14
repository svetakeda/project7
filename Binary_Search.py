import random


def Binary_Search(list, number, first_index, last_index):  # Binary Search with recursive
    if first_index > last_index:
        return None
    else:
        middle_number = (first_index + last_index) // 2    # Looking for middle number
        if number == list[middle_number]:
            return middle_number                           # Program stops if middle number = needed number
        elif number < list[middle_number]:                 # If number smaller or bigger it starts recursive again
            return Binary_Search(list, number, first_index, middle_number - 1)
        else:
            return Binary_Search(list, number, middle_number + 1, last_index)


def Binary_Search_2(list, number, first_index, last_index):  # Binary Search with iteration
    while first_index + 1 < last_index:
        middle_number = (first_index + last_index) // 2      # Looking for middle number
        if list[middle_number] < number:
            first_index = middle_number                      # First index becomes middle number
        else:
            last_index = middle_number
    return last_index


list = []                                                    # Making new list
for i in range(0, 100):
    list.append(random.randint(0, 100))
list.sort()
print(list)

number = int(input("Введите искомое число: "))
first_index = -1
last_index = len(list)
if number > last_index:
    print("None")
else:
    print(Binary_Search(list, number, first_index, last_index))
    print(Binary_Search_2(list, number, first_index, last_index))
