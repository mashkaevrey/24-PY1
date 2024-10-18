numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
first_list = sum(numbers[:4])
second_list = sum(numbers[5:])
suma = first_list + second_list
amount = len(numbers)
average = suma/amount
numbers[4] = average
print("Измененный список:", numbers)
