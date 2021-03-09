s = input('Enter a string: ')
longest = ''
current = ''

for i in range(len(s)):
    if s[i] >= s[i-1]:
        current += s[i]
    else:
        current = s[i]
    if len(current) >=len(longest):
        longest = current
print(longest)