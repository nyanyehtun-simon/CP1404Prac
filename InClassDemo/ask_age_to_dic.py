ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

name = input('Name: ')
age = int(input('Age: '))

ages_dict[name] = age

for key, val in ages_dict.items():
    print("{:10} - {:10}".format(key, val))
