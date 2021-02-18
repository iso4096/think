def find():
    fracs = []
    for i in range(10, 100):
        for j in range(10, 100):
            try:
                if i/j == (i//10)/(j%10) and i/j < 1:
                    fracs.append(str(i) + "/" + str(j))
            except:
                pass
    return fracs

def find_3():
    fracs = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            try:
                if i/j == int(str(i)[:1])/int(str(j)[1:]) and i/j < 1:
                    fracs.append(str(i) + "/" + str(j))
            except:
                pass
    return fracs

print(find())
print(find_3())