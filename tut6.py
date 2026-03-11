#find duplicate element in string

s = input()
sx = ""
for i in s:
    if i not in sx:
        sx +=i
    else:
        print("duplicate element in the string",i)
