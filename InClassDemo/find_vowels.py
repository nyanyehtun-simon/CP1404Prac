VOWELS = 'aeiou'
vowel_count = 0

original_name = input('Name: ')

name = original_name.lower()

for char in name:
    if char in VOWELS:
        vowel_count += 1

print("Out of {0} letters, {2} has {1} vowels".format(len(name), vowel_count, original_name))

