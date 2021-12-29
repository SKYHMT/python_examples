# def greater_user():
#     print("Hi world!")
#     print("I am Mandy")
#
#
# print("start")
# greater_user()
# print("finish")
# when another program need this infor, we can use this function to be added. Always defied the function first.
# we can set a parameter to a function:
def greater_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome to the world")


print("start")
greater_user(first_name="Mandy", last_name="He")
# make your code more readable, also can use mix mode, first use the potential argument, then use the actual argument
greater_user("Darren", "Huang")
print("finish")
# "Mandy" "He" and "Darren" "Huang" are arguments, and name is parameter.