# names = ["Jack", "Jill", "Harry"]
# dobs = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

import datetime
now = datetime.datetime.now()

name_dob_list = {}

while len(name_dob_list) < 1:
    name = input('Enter Name: ')
    dob = input('Enter Date of Birth: ')

    name_dob_list[name] = tuple(dob.split('/'))

for key, val in name_dob_list.items():
    print("{} is {} years old".format(key, now.year - int(val[2])))


