TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)


def turn(p1, p2, p3):
    """

    :param p1: point #1
    :param p2: point #2
    :param p3: point #3
    :return: -1 if clockwise rotate, 1 if counter clockwise rotate and 0 if point on a line
    """
    return cmp((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]), 0)


def angle_cmp(first_point):
    """

    :param first_point: lower left point
    :return: function for compare angles
    """
    def _angle_cmp(p1, p2):
        return turn(first_point, p1, p2)
    return _angle_cmp


def convex_hull(stack, next_point):
    """

    :param stack: current convex hull
    :param next_point: next point
    :return: stack considering next point
    """
    while len(stack) > 1 and turn(stack[-2], stack[-1], next_point) != TURN_LEFT:
        stack.pop()
    if not len(stack) or stack[-1] != next_point:
        stack.append(next_point)
    return stack


def graham_scan_1(points):
    """

    :param points: list of input points
    :return: convex hull (clockwise)
    """
    points.sort()
    first_point = points[0]
    points = points[1:]
    points.sort(angle_cmp(first_point), reverse=True)
    return reduce(convex_hull, points, [first_point])
