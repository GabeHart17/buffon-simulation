from polygon import NormalizedPolygon
from simulation import *
import matplotlib.pyplot as plt

MIN_LENGTH = 0.05
MAX_LENGTH = 2
INCREMENT = 0.05
NUM_TRIALS = 10000

circle = NormalizedPolygon.approximate_ellipse(0, 100)

length = MIN_LENGTH
lengths = []
probabilities = []
while length <= MAX_LENGTH:
    lengths.append(length)
    probabilities.append(buffon_probability(circle, length, NUM_TRIALS))
    length += INCREMENT

fig, ax = plt.subplots()
ax.plot(lengths, probabilities)
ax.set_title("Buffon Probability on Circle")
ax.set_xlabel("Needle Length")
ax.set_ylabel("Buffon Probability")
plt.show()
