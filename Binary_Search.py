import random

def Binary_Search(list, number, first_index, last_index):
    if first_index > last_index:
        return None
    else:
        middle_number = (first_index + last_index) // 2
        if number == list[middle_number]:
            return middle_number
        elif number < list[middle_number]:
            return Binary_Search(list, number, first_index, middle_number - 1)
        else:
            return Binary_Search(list, number, middle_number + 1, last_index)



def Binary_Search_2(list, number, first_index, last_index):
    while first_index + 1 < last_index:
        middle_number = (first_index + last_index) // 2
        if list[middle_number] < number:
            first_index = middle_number
        else:
            last_index = middle_number
    return last_index





list = []
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


