my_list = ["Apple", 2, 4, "Banana"]
country_name = ["France", "USA", "India", "India", "UK"]
my_list.extend(country_name)
# print(my_list)
country_name.append("Italy")
country_name.insert(2, "Mexico")
country_name.remove("Italy")
# country_name.clear()
country_name.pop()
print(country_name)
print(country_name.index("India"))
print(country_name.count("India"))
country_name.sort()
print(country_name)
country_name.reverse()
print(country_name)


my_number=[4, 78, 12, 41, 68]
my_number.sort()
print(my_number)
my_number.reverse()
print(my_number)

print("new list")
new_list = my_number.copy()
print(new_list)

