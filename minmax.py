#min and max elements in the list
s = list(input())
def min_ele():
    min = s[0]
    for i in range(len(s)):
        if min >= s[i]:
            s[i] = min
    return min
print(min_ele())