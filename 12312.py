def si(lis):
    s = []
    for x in range(len(lis)):
        if lis[x] == 0:
            s.append(0)
        else:
            for i in range(len(lis[x])):
                s.append(lis[x][i])
    s = sum(s)
    return s



def sheet_count(lis):
    count = 0
    while si(lis) != 0:
        lisAB = [[2745, 1220]]
        count += 1
        for j in range(len(lis)):
            for lcount in range(len(lisAB)):
                try:
                    if lis[j][0] <= lisAB[lcount][0] and lis[j][1] <= lisAB[lcount][1]:

                        a1 = lisAB[lcount][0] - lis[j][0]
                        b1 = lis[j][1]
                        b2 = lisAB[lcount][1] - lis[j][1]
                        a2 = lisAB[lcount][0]
                        if a1 < b1:
                            a1, b1 = b1, a1
                        if a2 < b2:
                            a2, b2 = b2, a2

                        lisAB.append([a1, b1])
                        lisAB.append([a2, b2])
                        lis[j] = 0
                        del lisAB[lcount]
                        # print(lis, '   ', lisAB)
                        break
                    else:
                        continue
                except:
                    continue
    return count


a=[[300,300] for i in range(50)]
print(a)
print(sheet_count(a))

if height <= 1220 and width <= 2745 and length <= 2745:
    lis = [[length, width], [length, height], [length, height], [width, height], [width, height]]

top = [length, width]
if 1220 < height <= 2745 and width <= 1220:
    side1 = [width,  ]