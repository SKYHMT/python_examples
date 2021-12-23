# for x in range(4):
#     for y in range(3):
#         print(f"({x}, {y})")
# excute x=0, y=0, then print; then excute second line: y=1
# exercise:
numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print("x" * x_count)
# multiple a shape by number, and the shape will repeat
# solution:
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output+="x"
    print(output)