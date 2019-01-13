names = ["Jack", "Jill", "Harry"]
dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

combo_dict = dict(zip(names, dobs))

for key, val in combo_dict.items():
    print(key, val)

