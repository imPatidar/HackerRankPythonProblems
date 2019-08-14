#Absolute
s=1
print(abs(s))

#Iterables
iterable="test1"
def all(iterable):
    for element in iterable:
        if not element:
            return False
        return True
#map
s=['10','2','2','54']
t = map(int,['10','2','2','54'])
print(t)