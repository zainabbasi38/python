#Strings are immutable
a = "!!!Zain !!!!!  !!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a)
print(a.count("!"))
print(a.split(" "))
print(a.rstrip("!"))
print(a.endswith("*!"))
print(a.endswith("!", 5, 11))
print(a.find("Zai"))
d = "      "
print(d.isspace())