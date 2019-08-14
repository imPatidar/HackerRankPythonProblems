for i in range(1,6):
    print(' '*(6-i)+'#'*i)

for i in range(1,6):
    print('#'*i+' '*(6-i))

for i in range(1,6):
    print(str(i)*i+' '*(6-i))

for i in range(1,6):
    print(' '*(6-i)+str(i)*i)

for i in range(5,0,-1):
    print(str(i)*(i)+' '*(5-i))

for i in range(5,0,-1):
    print(' '*(5-i)+str(i)*i)

#Star Pyramid

for i in range(5):
    print(' '*(5-i-1)+'*'*(2*i+1))

print()

for i in reversed(range(5)):
    print(' '*(5-i-1)+'*'*(2*i+1))
