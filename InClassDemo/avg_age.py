age_list = []
total = 0
age = int(input('Enter age: '))

while age >= 0:
    age_list.append(age)
    age = int(input('Enter age: '))

for i in range(len(age_list)):
    total += age_list[i]

avg_age = total / len(age_list)

print('Average age: {}'.format(avg_age))