import random
import copy

# 定義城市坐標
citys = [ 
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

# 創建城市索引列表
path = [i for i in range(len(citys))]

# 計算兩點之間的距離
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

# 創建城市之間的距離地圖
def distance_map():
    map = [[0 for _ in range(len(citys))] 
           for _ in range(len(citys))]
    for row in range(len(citys)):
        for col in range(len(citys)):
            map[row][col] = distance(citys[row], citys[col])
    return map

# 計算路徑的總距離
def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(1, plen):
        dist += distance(citys[p[i-1]], citys[p[i]])
    return dist

# 爬山演算法
def climb():
    router = path
    length = len(path)
    min_distance = pathLength(path)

    turn = 1000
    while turn:
        # 隨機選擇兩個城市進行交換
        p1 = int(random.random() * length)
        p2 = int(random.random() * length)
        while p1 == p2:
            p2 = int(random.random() * length)

        # 創建新路徑並計算新路徑的總距離
        new = copy.deepcopy(router)
        new[p1], new[p2] = new[p2], new[p1]
        curr_distance = pathLength(new)
        
        # 如果新路徑的距離更短，更新最小距離和路徑
        if curr_distance < min_distance:
            min_distance = curr_distance
            router = new
        turn -= 1
    print("爬山算法找到的最小距離:", min_distance)
    return router

print(climb())
