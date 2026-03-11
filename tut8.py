8#Check if two strings are anagrams
# sorted() is a Python built-in function used to arrange elements in order (ascending by default).

s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("string is anagram")
else:
    print("string is not anagram")

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