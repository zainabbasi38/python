a = int(input("Enter your age: "))
print("Your age is", a)

if a > 18:
    edu = int(input("Enter your edu in numbers: "))
    if edu >=12:print("You can drive")

elif a <0:
    print("Age is not valid")
else:
    print("You cannot drive")
print("Yes")
    