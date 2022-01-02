try:
    age = int(input("Age: "))
    income = 20000
    rish = income / age
    print(age)
except ZeroDivisionError:
    print("Age canno't be 0.")
except ValueError:
    print("Invalid value")

# if inputer no value, would crash the program.
