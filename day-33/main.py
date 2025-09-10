student = {
    "name": "John Doe",
    "age": 21,
    "courses": ["Math", "CompSci"]
}
# print(student)
# print(student["name"])
# print(student["name2"])
# print(student.get("name2"))
# for key in student.keys():
#     print(key)
for key , value in student.items():
    print(f"{key}: {value}")

for course in student["courses"]:
    print(course)