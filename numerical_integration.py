import random
import math
from polygon import NormalizedPolygon
from simulation import *

# f: integrand function
# bounds: 2-dimensional float array of integration bounds
def monte_carlo_integrate(f, bounds, num_trials):
    normalization = 1 / num_trials
    for b in bounds:
        normalization *= b[1] - b[0]
    acc = 0
    for i in range(num_trials):
        point = [random.uniform(b[0], b[1]) for b in bounds]
        acc += f(*point)
    return acc * normalization

if __name__ == '__main__':
    l = 0.1
    f = lambda theta, s: (l - s) * math.sin(theta + math.asin(((l-s) / l) * math.sin(theta)))
    delta = lambda s,h,theta: (h * l) / f(theta, s)
    indicator = lambda theta: lambda q,h,s: 1 if h < f(theta, s) and q < l - delta(s,h,theta) else 0
    integrand = lambda theta: lambda q,h,s: (1 / l) * (1 - (((l-s)**2)/l**2) * math.sin(theta)**2)**(-0.5)
    # square with sides of pi/2
    n_samples = 10000
    m2 = 4 * 2 * monte_carlo_integrate(lambda q,h,s: indicator(math.pi/2)(q,h,s)*integrand(math.pi/2)(q,h,s), [[0,l],[0,l],[0,l]], n_samples)
    N = 2 * math.pi * (math.pi / 2)**2 + 4 * math.pi * l
    M = 8 * math.pi * l
    m1 = M - 2 * m2
    sigma = N - m1 - m2
    # prob = sigma / (sigma + m1)
    prob = sigma / (sigma + (m1/2))
    print(f'integration method: {prob}')

    poly = NormalizedPolygon.regular(4)
    prob_actual = buffon_probability(poly, l, 100000)
    print(f'actual probability: {prob_actual}')
