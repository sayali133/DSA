2# check a string is pallindrome or not

s = input()
if s == s[::-1]:
    print("pallindrome")
else:
    print("Not pallindrome")
