from graham_scan.solve1 import convex_hull


def graham_scan_2(points):
    points = sorted(points)
    l = reduce(convex_hull, points, [])
    u = reduce(convex_hull, reversed(points), [])
    return l.extend(u[i] for i in xrange(1, len(u) - 1)) or l
