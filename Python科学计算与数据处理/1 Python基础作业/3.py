S = "Spam"


for c in S:
    print("'" + c + "'的ASCII码是", ord(c))


asciiSum = 0
for c in S:
    asciiSum += ord(c)
asciiSum


asciis = []
for c in S:
    asciis.append(ord(c))
asciis

map(ord, S)
