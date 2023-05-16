import random
import math
from polygon import NormalizedPolygon

def buffon_trial(polygon, needle_size):
    x = polygon.sample()
    theta = random.uniform(0, 2*math.pi)
    y = (x[0] + needle_size * math.cos(theta), x[1] + needle_size * math.sin(theta))
    return polygon.contains(y), x, y

def buffon_probability(polygon, needle_size, num_trials):
    successes = 0
    for i in range(num_trials):
        successes += buffon_trial(polygon, needle_size)[0]
    return successes / num_trials

