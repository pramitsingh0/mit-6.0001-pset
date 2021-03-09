s = input(("Enter lowercase characters:"))
count = 0

for bob in range(len(s)-2):
    if 'bob' in s[bob:bob+3]:
        count += 1

print("number of bobs: ", count)
