# >=, <=, ==, !=(not equal) but = do not work as it is set the temperature 30, not comparision with other value.
# temperature = 40
# if temperature > 30:
#     print("It is a hot day")
# else:
#     print("It is not a hot day")
name_characters_long = 89
# if name_characters_long < 3:
#     print(" Name must be at least 3 characters")
# elif name_characters_long > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")
# name = "Ma"
# if len(name)<3:
#     print("Name must be at least 3 characters")
# elif len(name) > 50:
#     print("Name can be a maximum of 50 characters")
# else:
#     print("Name looks good")

# project: weight convert
# W=input("Weight: ")
# unit=input("(L)bs or (K)g: ")
# W1=W*float(0.23)
# W2=W*23
# if unit == L:
#     print("You are" + W1 +"kilogram")
# else:
#     print("You are" + W2 + "pounds")

# solution:
# weight = int(input("Weight: "))
# unit = input("(L)bs or (K)g: ")
# if unit == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight // 0.45 (// get integer)
#     print(f"You are {converted} pounds")
# (input always return to the string, use int to return it to integer)
# (formatted: f" {}")