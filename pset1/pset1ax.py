s = input(("Enter lowercase characters:"))
count = 0
vowels = ['a', 'u', 'o', 'i', 'e']

for char in s:
    if char in vowels:
        count += 1

print("number of vowels: ", count)