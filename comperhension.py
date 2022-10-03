

numbers = [1, 2, 4, 4, 7]

numbers_sq = []

for item in numbers:
    numbers_sq.append(item ** 2)
print(numbers_sq)

print('-'*20)

number_sq_2 = [item ** 2 for item in numbers]  # list comprehension
print(number_sq_2)

print('-'*20)

number_sq_3 = (item ** 2 for item in numbers)  # generator comprehension
print(number_sq_3)
for item in number_sq_3:
    print(item)

print('-'*20)
number_sq_4 = tuple(item ** 2 for item in numbers)
print(number_sq_4)

print('-'*20)
number_sq_5 = set(item ** 2 for item in numbers)
print(number_sq_5)
