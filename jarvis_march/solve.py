TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)
 

def turn(p1, p2, p3):
    return cmp((p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1]), 0)
 

def _dist(p1, p2):
    """

    :param p1: point #1
    :param p2: point 2
    :return: the squared Euclidean distance between p1 and p2
    """
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def next_point(points, last_point):
    new_point = last_point
    for p in points:
        t = turn(last_point, new_point, p)
        if t == TURN_RIGHT or t == TURN_NONE and _dist(last_point, p) > _dist(last_point, new_point):
            new_point = p
    return new_point


def jarvis_march(points):
    hull = [min(points)]
    for point in hull:
        np = next_point(points, point)
        if np != hull[0]:
            hull.append(np)
    return hull
