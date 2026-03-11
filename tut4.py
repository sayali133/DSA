4#check vowels and consonants in the string

s = input()
v = "aeiouAEIOU"
vowels = " "
consonants = " "
for i in s:
    if i in v:
        vowels += i
    else:
        consonants +=i

print("vowels",vowels)
print("consonants",consonants)

