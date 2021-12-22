# and  indicate both conditions are true
# or at least one condition is true
# not one is true and another is certainly not true
# EX: Mandy is smart and hardworking (and didn't fail any courses)
#     Mandy is a good student
is_smart = True
fail_any_courses = True
if is_smart and not fail_any_courses:
    print("Mandy is a good student")