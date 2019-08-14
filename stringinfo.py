s = "HelLoWoRLd"
m = ""
for i in range(97, 123):
    for letter in s:
        if letter == chr(i) or letter == chr(i).upper():
            m = m + letter
print(m)