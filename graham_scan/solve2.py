from graham_scan.solve1 import convex_hull


def graham_scan_2(points):
    points = sorted(points)
    lower = reduce(convex_hull, points, [])
    upper = reduce(convex_hull, reversed(points), [])
    return lower + upper[1:-1]
