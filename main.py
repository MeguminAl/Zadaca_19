i = 0

while True:
    uslovie1 = i % 19 == 0
    uslovie2 = str(i)[-2:] == '19'
    x = str(i)
    xx = []
    for q in x:
        xx.append(int(q))
    z = sum(xx)
    uslovie3 = z == 19
    if uslovie1 == True and uslovie2 == True and uslovie3 == True:
        print(i)   
        break
    i += 1
