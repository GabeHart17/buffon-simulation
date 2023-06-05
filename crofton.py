import random
import math
from polygon import *

def segments_intersect(s1, s2):
    x1 = s1[0][0]
    x2 = s1[1][0]
    x3 = s2[0][0]
    x4 = s2[1][0]
    y1 = s1[0][1]
    y2 = s1[1][1]
    y3 = s2[0][1]
    y4 = s2[1][1]
    d = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    tn = (x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
    un = (x1-x3)*(y1-y2)-(y1-y3)*(x1-x2)
    t = tn/d
    u = un/d
    return 0 <= t <= 1 and 0 <= u <= 1


class CroftonEstimator:
    def __init__(self, curve, bounds, length):
        self.curve = curve
        self.bounds = bounds
        self.length = length

    def crofton_trial(self):
        x = (random.uniform(bounds[0], bounds[1]), random.uniform(bounds[2], bounds[3]))
        theta = random.uniform(0, 2*math.pi)
        y = (x[0] + self.length * math.cos(theta), x[1] + self.length * math.sin(theta))
        count = 0
        for segment in self.curve:
            if (segments_intersect((x,y), segment)):
                count += 1
        return count

if __name__ == '__main__':
    # curve = [((0,-0.5),(0,0.5))]
    circle_poly = NormalizedPolygon.approximate_ellipse(0, 100)
    shifted_vertices = circle_poly.vertices[1:] + [circle_poly.vertices[0]]
    curve = list(zip(circle_poly.vertices, shifted_vertices))
    bounds = [-1, 1, -1, 1]
    length = 1
    estimator = CroftonEstimator(curve, bounds, length)
    ms = {}
    n_samples = 100000
    for i in range(n_samples):
        n = estimator.crofton_trial()
        if n not in ms.keys():
            ms[n] = 1
        else:
            ms[n] += 1
    for key in sorted(ms.keys()):
        print(key, (ms[key] / n_samples) * ((bounds[1] - bounds[0]) * (bounds[3] - bounds[2]) * 2 * math.pi))
    length = 0
    for a,b in curve:
        length += math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2)
    print(length)
