# class Pallet_calculate:
#     def __init__(self, ):
import random

def decor(fun):
    def wrap(*args,**kwargs):
        c=[]
        for i in range(1000):
            c.append(fun(*args,**kwargs))
        return max(c)
    return wrap
@decor
def sq1(aa, ab, alA, alB):

    c = []
    def sq(a=aa, b=ab, lA=alA, lB=alB, count=0):
        nonlocal c
        if lA < lB:
            lA, lB = lB, lA
        if a > lA or b > lB:
            return 0
        c.append(1)
        m=random.randint(0,1)
        if m:
            lA1 = lA - a
            lB1 = lB
            lA2 = a
            lB2 = lB - b

        else:
            lA1 = lA - a
            lB1 = b
            lA2 = lA
            lB2 = lB - b
        l1 = sq(a, b, lA1, lB1, count)
        l2 = sq(a, b, lA2, lB2, count)
        # print(m)
        return c
    return sum(sq())



print(sq1(200,150, 2000,1200))
