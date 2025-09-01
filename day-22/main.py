marks = [30,50,70,90,100]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2]) 

name = "Zain"
listing = [name]
if "Zain" in listing:
    print("Yes, 'Zain' is in the list")
colors = ['red','green','blue','yellow']
print(colors)
print(type(colors))
print(colors[-1])
print(colors[len(colors)-2])
print(colors[-3])
print(colors[-4])



lst = [i for i in range(5)]
print(lst)
lst = [i for i in range(10) if i%2==0]
print(lst)