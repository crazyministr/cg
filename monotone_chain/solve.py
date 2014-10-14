def turn(p1, p2, p3):
    return cmp((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]), 0)


def convex_hull(hull, point):
    while len(hull) > 1 and turn(hull[-2], hull[-1], point) <= 0:
        hull.pop()
    if not len(hull) or hull[-1] != point:
        hull.append(point)
    return hull


def monotone_chain(points):
    points = sorted(points)
    return reduce(convex_hull, points, []) + reduce(convex_hull, reversed(points), [])[1:-1]
