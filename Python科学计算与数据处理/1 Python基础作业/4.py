D = {'f':6, 'c':3, 'a' :1, 'g':7, 'e':5, 'd':4, 'b':2}

sortedKeys = sorted(D.keys())
for k in sortedKeys:
    print(k, ":", D[k])