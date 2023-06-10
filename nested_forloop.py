# first_list = ["a", "b", "c", "d", "e"]
# second_list = ["Mahesh", "Suresh", "Kamlesh", "Rajesh", "Lokesh"]
# for letter in first_list:
#     for name in second_list:
#         print(f"{letter}) {name}")

twoD_list = [[1, 2, 3, 4],
             [1, "Apple", 3],
             [1, True]
            ]
for row in twoD_list:
    for col in row:
        print(col)