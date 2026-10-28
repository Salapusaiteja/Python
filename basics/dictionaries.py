student = {
    "name": "Sai Teja",
    "age": 23,
    "course": "Python"
}
print(student["name"])  # Sai Teja
print(student["age"])  # 22
student["city"] = "Visakhapatnam"
print(student)  # {'name': 'Sai Teja', 'age': 22, 'course': 'Python', 'city': 'Visakhapatnam'}
student.pop("course")
print(student) #{'name': 'Sai Teja', 'age': 23, 'city': 'Visakhapatnam'}
