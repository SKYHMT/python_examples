# customer = {
#     "name": 'Mandy He',
#     "age": 20,
#     "is_verified": True
# }
# print(customer["name"])
# print(customer.get("birthday"))
# customer["birthday"] = "Jan, 1st, 1996"
# print(customer["birthday"])
# every atribute should be uqnic
# exercise: phone: 1234, print: one, two, three, fuor
phone = input("Phone: ")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output = output + digits.get(ch, " unknown")+" "
print(output)