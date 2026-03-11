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

6#find duplicate element in string

"""
s = input()
sx = ""
for i in s:
    if i not in sx:
        sx +=i
    else:
        print("duplicate element in the string",i)
"""
7#Reverse a string without using slicing

"""
s = input()
rev = ""
for i in s:
    print(i)
    rev = i + rev
print(rev)
"""

8#Check if two strings are anagrams
# sorted() is a Python built-in function used to arrange elements in order (ascending by default).
"""
s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("string is anagram")
else:
    print("string is not anagram")
"""
#without using built in methods
"""
s1 = input()
s2 = input()

if len(s1) != len(s2):
    print("not anagram")
else:
    for i in s1:
        if s1.count(i) != s2.count(i):
            print("not anagrams")
            break
    else:
        print("anagram")


"""




























