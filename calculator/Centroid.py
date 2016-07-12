from classify import Point

class Centroid:
    def __init__(self):
        self.points = []
        
    def polygonRing(self, ring):
        arr = ring.split(' ')

        points = []

        for idx in range(len(arr)/2):
            x = float(arr[idx*2])
            y = float(arr[idx*2 + 1])
            p = Point.Point(x, y)
            points.append(p)

        self.points = points
    
    """计算平面点坐标集合中心（非质心）"""
    def calculate(self):
        mx = 0
        my = 0
        ma = 0

        for idx in range(len(self.points)-1):
            p1 = self.points[idx]
            p2 = self.points[idx+1]

            mx = mx + (p1.x + p2.x) * (p1.x * p2.y - p2.x * p1.y)
            my = my + (p1.y + p2.y) * (p1.x * p2.y - p2.x * p1.y)

            ma = ma + (p1.x * p2.y - p2.x * p1.y)

        if ma == 0:
            return "-1"

        a = 0.5 * ma
        cx = mx / (6 * a)
        cy = my / (6 * a)

        return "a:" + str(a) + " x:" + str(cx) + " y:" + str(cy)