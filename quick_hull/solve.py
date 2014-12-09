from math import sqrt


class Line():
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.a = r[1] - l[1]  # y2 - y1
        self.b = l[0] - r[0]  # x1 - x2
        self.c = -self.a * l[0] - self.b * l[1]  # c = -a * x1 - b * y1

    def is_left(self, p):
        return self.a * p[0] + self.b * p[1] + self.c < 0

    def is_right(self, p):
        return self.a * p[0] + self.b * p[1] + self.c > 0

    def dist(self, p):
        return float(abs(self.a * p[0] + self.b * p[1] + self.c)) / sqrt(self.a * self.a + self.b * self.b)


def _quick_hull(convex_hull, line, points):
    if len(points) == 0:
        convex_hull.append(line.r)
        return

    next_line = Line(line.l, points[0])
    next_point = points[0]
    max_dist = line.dist(points[0])
    for point in points[1:]:
        dist = line.dist(point)
        if dist > max_dist:
            max_dist = dist
            next_point = point
            next_line = Line(line.l, point)
        elif dist == max_dist and next_line.is_left(point):
            next_point = points
            next_line = Line(line.l, point)

    line1 = Line(line.l, next_point)
    line2 = Line(next_point, line.r)
    points1 = [point for point in points if line1.is_left(point)]
    points2 = [point for point in points if line2.is_left(point)]
    _quick_hull(convex_hull, line1, points1)
    _quick_hull(convex_hull, line2, points2)


def quick_hull(points):
    points = [(x, y) for x, y in points]  # [[], [], ..] -> [(), (), ...]
    points = list(set(points))  # remove the same points
    if len(points) < 3:
        return points

    line = Line(min(points), max(points))
    up = [point for point in points if line.is_left(point)]
    down = [point for point in points if line.is_right(point)]
    convex_hull = []
    _quick_hull(convex_hull, line, up)
    line = Line(max(points), min(points))
    _quick_hull(convex_hull, line, down)
    print convex_hull
    return convex_hull
