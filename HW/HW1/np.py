#本程式參考
#https://blog.csdn.net/zw17302560727/article/details/122304577
#和
#https://github.com/ccc112b/py2cs/blob/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/02-%E5%84%AA%E5%8C%96%E7%AE%97%E6%B3%95/01-%E5%82%B3%E7%B5%B1%E5%84%AA%E5%8C%96%E6%96%B9%E6%B3%95/01-%E5%84%AA%E5%8C%96/01-%E7%88%AC%E5%B1%B1%E6%BC%94%E7%AE%97%E6%B3%95/03-%E9%80%9A%E7%94%A8%E7%9A%84%E7%88%AC%E5%B1%B1%E6%A1%86%E6%9E%B6/tsp.py進行修改
import random
import copy
import math

citys = [ 
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

path = [i for i in range(len(citys))]
#print(path)

def distance(p1, p2): #計算兩點距離
    #print('p1=', p1)
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def pathLength(p): #計算總距離
    dist = 0
    plen = len(p)
    #print(plen)
    for i in range(1,plen):
        dist += distance(citys[p[i-1]], citys[p[i]])
        #print(dist)
    return dist

def climb():
    router = path
    length = len(path)
    distance = pathLength(path)

    turn = 1000
    while turn:
        p1 = int(random.random() * length)
        p2 = int(random.random() * length)
        while p1 == p2:
            p2 = int(random.random() * length)

        new = copy.deepcopy(router)
        new[p1],new[p2] = new[p2],new[p1]
        curr_distance = pathLength(new)
        if curr_distance < distance:
            distance = curr_distance
            router = new
        turn -= 1
    print("climb總距離：", distance)
    return router
#print('pathLength=', pathLength(path))
print(climb())