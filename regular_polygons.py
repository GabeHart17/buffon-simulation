from polygon import NormalizedPolygon
from simulation import *
import matplotlib.pyplot as plt

MIN_SIDES = 3
MAX_SIDES = 10
NEEDLE_LENGTH = 0.1
NUM_TRIALS = 500000

side_counts = []
probabilities = []

for n in range(MIN_SIDES, MAX_SIDES + 1):
    side_counts.append(n)
    poly = NormalizedPolygon.regular(n)
    probabilities.append(buffon_probability(poly, NEEDLE_LENGTH, NUM_TRIALS))

fig, ax = plt.subplots()
ax.plot(side_counts, probabilities)
ax.set_title('Buffon Probability on Regular Polygons')
ax.set_xlabel('number of sides')
ax.set_ylabel('probability')

plt.show()
