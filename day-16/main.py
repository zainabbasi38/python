x = int(input("ENter the value of x: "))

match x:

    case 0:
        print("X is zero")
    case 1:
        print("X is one")
    case 10:
        print("X is ten")
    # case _ if x!=90:
    #     print(f"X is 80")
    # case _ if x!=80:
    #     print(f"X is 90")
    case _:
        print(f"X is {x}")
    