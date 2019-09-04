# Using Inbuilt Function
c = "This is a python code. is it True?"
ss = "is"

count = c.count(ss)
print(count)


# Without Using Inbuilt Function

count = 0
string = "This is a python code. is it True?"
substring = "is"
for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        count += 1
print(count)