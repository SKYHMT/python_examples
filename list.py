# names = ["Mandy", "Darren", "Max", "Jackson", "Kelsey"]
# # print(names[3:])
# names[0] = "Mady"
# print(names)
# exercise: the largest number in a list
# numbers = [2,5,7,3,9,1,4]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
#
# 2D_lists:
# matrix= [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# # matrix [1][2] = 12 (could be modify)
# # print(matrix[1][2])
# # inner loops:
# for row in matrix:
#     for item in row:
#         print(item)

# list_methods:
# numbers = [1, 4, 8, 5, 9, 10]
# numbers.append(3)
# print(numbers)
# numbers.insert(2, 3)
# print(numbers)
# numbers.clear()
# print(numbers)
# print(numbers.index(9))
# print(20 in numbers)
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()
# numbers.append(90)
# print(numbers2) (not impact the copy line)
# exercise: remove the duplicates in a list:
numbers = [2, 4, 3, 6, 12, 4, 3, 9]
# for number in numbers:
#     if item in number:
#         numbers.remove(item)
# print(item)
new = []
for number in numbers:
    if number not in new:
        new.append(number)
print(new)