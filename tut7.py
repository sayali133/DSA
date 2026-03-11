7#Reverse a string without using slicing

s = input()
rev = ""
for i in s:
    print(i)
    rev = i + rev
print(rev)

