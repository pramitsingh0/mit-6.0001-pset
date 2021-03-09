s = input('Enter a string: ')
count = 0
maxcount = 0
result = 0
for char in range(len(s)-1):
    if s[char] < s[char + 1]:
        count += 1
        if count > maxcount:
            maxcount = count
            result = char+1
    else:
        count = 0
    
start = maxcount - char
print(s[start:maxcount])
