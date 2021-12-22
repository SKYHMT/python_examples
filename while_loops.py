# i = 1
# while i <= 5:
#     print(i)
#     i = i+1
# print("Done")
# excute a block of code multiple times
# i = 1
# while i <= 5:
#     print("*" * i)
#     i = i+1
# print("Done")
# when a string multiple a number, the string will be repeated

# use y loop build a guessing game:
# x = 9
# number = input("x: ")
# while x != 9:
#     print("You failed")
# else:
#     print("You win")

# solution:
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("Guess: "))
#     guess_count +=1
#     if guess == secret_number:
#         print("You won!")
#         break
# else:
#     print("You failed!")
#
# y loop: excute code multiple times, and i is a condition. Use break to shut down the program.

# excise: car game:
# help = input("> ")
# print("start-to start the car")
# print("stop-to stop the car")
# print("quit- to exit")
# start = input("> ")
# stop = input("> ")
# quit = input("> ")
# while
#     print("Car started...Ready to go!")

# Solution:
command = ""
started = False
while command != "quit":
    command = input("> ")
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
    """)
    elif command == "quit":
        break
    else:
        print("Sorry, it can't understand...")
