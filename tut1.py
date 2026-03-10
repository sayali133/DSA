1#reverse a string with sliceing
"""
s = input()
print(s[::-1])

"""
2# check a string is pallindrome or not
"""
s = input()
if s == s[::-1]:
    print("pallindrome")
else:
    print("Not pallindrome")

"""

3#count vowels and consonants in the string
"""
s = input()
v = "aeiouAEIOU"
vc = 0
c = 0
for i in s:
    if i in v:
        vc +=1
    else:
        c +=1
print("count of vowels:",vc)
print("count of consonents:",c)

"""

4#check vowels and consonants in the string
"""
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

"""
         
5#Count frequency of characters in the string 
"""
s = input()      
for i in set(s):
    count = 0
    for j in s:
        if i == j:
            count +=1
    print("elements",i,"count",count)
"""

    




 

