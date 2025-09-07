info = "My name is {} and i am from {}"
name = "Zain"
country = "Pakistan"
# print(info.format(name, country))
print(info.format(country, name))

info = f"My name is {name} and i am from {country}"
print(info)

price = 99.0000
print(f"The price is {price:.2f}")  # limit to 2 decimal places

print(f"{2*60}")