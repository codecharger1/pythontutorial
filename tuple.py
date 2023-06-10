# my_list = [ "Apple", 2, 4, True, "Banana"  ]
# my_tuple = ("Apple", 2, 4, True, "Banana")
#
# print(my_tuple.count("Apple"))
# print(type(my_tuple))
# print(my_tuple[0:2])
# print(my_tuple)

# favourite_subject = ("Hindi", "English", "Science", "Mathematics", "Biology")
# Lokesh, Kamlesh, Mahesh, *other = favourite_subject
# print(other)

student_info = [
    ("Mahesh", 20, "India"),
    ("Tom", 18, "USA"),
    ("Hardy", 41, "UK")
]

for name, age, country in student_info:
    print(f"Student name: {name}, Age:{age}, Country:{country} ")