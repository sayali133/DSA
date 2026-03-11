5#Count frequency of characters in the string 

s = input()      
for i in set(s):
    count = 0
    for j in s:
        if i == j:
            count +=1
    print("elements",i,"count",count)
