

def s_count(length, width, height, ss, qq,sss,qqq):
    length += 106
    width += 106
    height += 50




    def brusCalculation(lis):
        count1 = 0
        while sum(lis):
            count1 += 1
            BRUS = 3000
            for i in range(len(lis)):
                if lis[i] <= BRUS:
                    BRUS -= lis[i]
                    lis[i] = 0
                else:
                    continue

        return count1



    lis=[]
    brus_lis = []
    if (height <= 1220 and width<=2745 and length<=2745) or (height <= 2745 and width<=1220 and length<=1220):
        lis = [[length, width], [length, height], [length, height], [width, height], [width, height]]
        for n in range(8):
            brus_lis.append(height)
        for p in range(4):
            brus_lis.append(width - 100)
        for p in range(4):
            brus_lis.append(length - 100)
        print(1)
    elif (height >= 1220 and 0<width<=2745 and 0<length<=2745):
        lis = [[length, width], [length, 1220], [length, 1220], [width, 1220], [width, 1220], [length, height - 1220],
               [length, height - 1220], [width, height - 1220], [width, height - 1220]]
        for n in range(8):
            brus_lis.append(height)
        for p in range(6):
            brus_lis.append(width - 100)
        for p in range(6):
            brus_lis.append(length - 100)
        print(2)


    br = brusCalculation(brus_lis)


    for i in lis:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]

    # print(lis)
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

    sh_width = ss
    sh_height = qq

    def sheet_count(lis,sh_width, sh_height):
        aa=sh_width
        bb=sh_height
        count = 0
        while si(lis) != 0:
            lisAB = [[aa, bb]]
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

    count = sheet_count(lis,sh_width, sh_height)
    hs = height + 9

                                                        # Расчет фанеры 9 мм
    c=[]
    def sq(a, b, lA, lB, count=0):
        if lA < lB:
            lA, lB = lB, lA
        if a > lA or b > lB:
            return 0
        c.append(1)
        lA1 = lA - a
        lB1 = lB
        lA2 = a
        lB2 = lB - b
        l1 = sq(a, b, lA1, lB1, count)
        l2 = sq(a, b, lA2, lB2, count)
        return c
    fanera9Count=1/(sum(sq(length,width, sss, qqq)))


    return [br, count, length, width, hs, fanera9Count]


def getBoxCount(l, w, h, rad, h_sheet, w_sheet):
    hh=h_sheet
    ww=w_sheet
    if rad==0:
        l_box=l
        w_box=w
        h_box=h
    elif rad==1:
        l_box = l+15
        w_box = w+15
        h_box = h+15
    elif rad == 2:
        l_box = l+25
        w_box = w+25
        h_box = h+25


    # dimensions of the scan
    l_tongue = 40

    h_scan = w_box + h_box
    w_scan = l_tongue + w_box * 2 + l_box * 2

    if (h_scan <= h_sheet) and (w_scan <= w_sheet):

        def cut(h_s=h_scan, w_s=w_scan, l_b=l_box, w_b=w_box, h_b=h_box):
            l_cut = ((h_s + w_s) * 2 + w_b * 6) + (h_b * 4 + l_b * 4 + w_b * 4)
            return (l_cut)
        w_surplus=None
        h_sheet = hh
        w_sheet = ww
        i = 0
        while w_sheet >= w_scan:
            while h_sheet >= h_scan:
                i = i + 1
                h_sheet = h_sheet - h_scan
            h_sheet = hh
            w_surplus = w_sheet - w_scan
            w_sheet = w_surplus

        w_sheet = h_sheet
        h_sheet = w_surplus

        while w_sheet >= w_scan:
            while h_sheet >= h_scan:
                i+=1
                h_sheet = h_sheet - h_scan
            h_sheet = w_surplus
            w_surplus2 = w_sheet - w_scan
            w_sheet = w_surplus2
        c = round(cut()/1000,2)
        s = round(1 / i,3)
        return [i, s, c, l_box, w_box, h_box]

    else:
        return False

def brusCalculation(args):
    lis = args.split(',')

    lis=[int(i) for i in lis]
    count1 = 0
    while sum(lis):
        count1 += 1
        BRUS = 3000
        for i in range(len(lis)):
            if lis[i] <= BRUS:
                BRUS -= lis[i]
                lis[i] = 0
            else:
                continue

    return count1

def brusCalculation1(args):
    lis =args
    for m in range(len(lis)):
        if lis[m]>3000:
            return False
    lis=[int(i) for i in lis]
    count1 = 0
    while sum(lis):
        count1 += 1
        BRUS = 3000
        for i in range(len(lis)):
            if lis[i] <= BRUS:
                BRUS -= lis[i]
                lis[i] = 0
            else:
                continue

    return count1




