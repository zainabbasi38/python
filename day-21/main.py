# def average(a = 9, b=9):
#     print("Average:", (a+b)/2)

# def name(first_name, last_name):
#     print("My first name", first_name, "and my last name is", last_name)


# name(first_name="Zain", last_name="Abbasi")

def average(*numbers):
    print("Average:", sum(numbers)/len(numbers))
average(3,5,6,2,7,4)

def name(**names):
    print(names["first_name"], names["last_name"])

def student(**students):
    print(students["student1"])
    print(students["student2"])

student(student1="Zain", student2="Ali")

name(first_name="Zain", last_name="Abbasi")

# average(2,6)
# average(b=6)
# average(b=6, a=2)

