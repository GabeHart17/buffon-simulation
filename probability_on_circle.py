from polygon import NormalizedPolygon
from simulation import *

NUM_SIDES = 100
NUM_TRIALS = 10000
NEEDLE_LENGTH = 0.1

poly = NormalizedPolygon.regular(NUM_SIDES)

print(buffon_probability(poly, NEEDLE_LENGTH, NUM_TRIALS))

for i in range(1,100):
    nl = 0.01*i
    p = buffon_probability(poly, nl, NUM_TRIALS)
    estimate = (math.pi - 2*nl + nl**2) / (math.pi + 2*nl - nl**2)
    print(0.01*i, p, estimate, p-estimate, sep=' , ')
