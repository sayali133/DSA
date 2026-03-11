3#count vowels and consonants in the string

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

