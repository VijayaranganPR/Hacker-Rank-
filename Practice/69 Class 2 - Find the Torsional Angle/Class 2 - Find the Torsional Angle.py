import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        vector1 = [self.x, self.y, self.z]
        vector2 = [no.x, no.y, no.z]
        return Points(*[x1 - x2 for x1, x2 in zip(vector1, vector2)])
        
    def dot(self, no):
        vector1 = [self.x, self.y, self.z]
        vector2 = [no.x, no.y, no.z]
        return sum(x1 * x2 for x1, x2 in zip(vector1, vector2))
        
    def cross(self, no):
        vector1 = [self.x, self.y, self.z]
        vector2 = [no.x, no.y, no.z]
        x = (vector1[1] * vector2[2]) - (vector1[2] * vector2[1])
        y = (vector1[2] * vector2[0]) - (vector1[0] * vector2[2])
        z = (vector1[0] * vector2[1]) - (vector1[1] * vector2[0])
        return Points(x, y, z)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))