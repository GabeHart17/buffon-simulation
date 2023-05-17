import random
import math

class NormalizedPolygon:
    def __init__(self, vertices):
        self.unscaled_vertices = vertices  # sequence of real-valued pairs, convexity left to user
        self.unscaled_perimeter = sum([math.dist(x,y) for x,y in zip(vertices, vertices[1:]+[vertices[0]])])
        scale_factor = 2 * math.pi / self.unscaled_perimeter
        self.vertices = [[j * scale_factor for j in i] for i in self.unscaled_vertices]

    def regular(num_vertices):
        vertices = []
        for i in range(num_vertices):
            theta = (2 * math.pi * i) / num_vertices
            vertices.append([math.sin(theta), math.cos(theta)])
        return NormalizedPolygon(vertices)

    def approximate_ellipse(eccentricity, num_vertices):
        thetas = [(2*math.pi*i)/num_vertices for i in range(num_vertices)]
        radii = map(lambda t: 1 / math.sqrt(1 - (eccentricity * math.cos(t))**2), thetas)
        vertices = [(r * math.cos(t), r * math.sin(t)) for r,t in zip(radii, thetas)]
        return NormalizedPolygon(vertices)

    def line_through_points(a,b):
        m = (b[1]-a[1])/(b[0]-a[0])
        b = a[1] - m * a[0]
        return lambda x: b + (m * x)

    def triangle_contains(vertices, p):
        for i in range(3):
            a = vertices[i-2]
            b = vertices[i-1]
            c = vertices[i]
            if a[0] == b[0]:  # case where triangle has vertical side, avoid zero division
                if (p[0] - a[0]) * (c[0] - a[0]) < 0:
                    return False
            else:
                f = NormalizedPolygon.line_through_points(a, b)
                if (p[1]-f(p[0]))*(c[1]-f(c[0])) < 0:  # if sign is positive, then on same side of line
                    return False
        return True

    def triangle_sample(vertices):
       a = vertices[0]
       b = (vertices[1][0] - a[0], vertices[1][1] - a[1])
       c = (vertices[2][0] - a[0], vertices[2][1] - a[1])  # move origin to a
       x = random.uniform(0, 1)
       y = random.uniform(0, 1)
       p = (x*b[0] + y*c[0], x*b[1] + y*c[1])  # random point in parallelogram
       if NormalizedPolygon.triangle_contains([(0,0),b,c], p):
           # point is in the triangle
           return (p[0] + a[0], p[1] + a[1])
       # point is in similar triangle forming other part of parallelogram
       p_prime = (b[0] + c[0] - p[0], b[1] + c[1] - p[1])
       return (p_prime[0] + a[0], p_prime[1] + a[1])

    def contains(self, p):  # p is coordinate pair
        for a,b in zip(self.vertices[1:-1], self.vertices[2:]):
            if NormalizedPolygon.triangle_contains([a,b,self.vertices[0]],p):
                return True
        return False

    def sample(self):
        triangle_areas = []
        a = self.vertices[0]
        for b,c in zip(self.vertices[1:-1], self.vertices[2:]):
            nb = (b[0]-a[0], b[1]-a[1])  # translate st. a is at origin
            nc = (c[0]-a[0], c[1]-a[1])
            det = nb[0]*nc[1] - nb[1]*nc[0]
            triangle_areas.append(abs(det))
        r = random.uniform(0, sum(triangle_areas))
        acc = triangle_areas[0]
        idx = 0
        while acc < r:
            idx += 1
            acc += triangle_areas[idx]
        return NormalizedPolygon.triangle_sample([a, self.vertices[idx+1], self.vertices[idx+2]])
