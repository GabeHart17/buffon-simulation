# from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from polygon import NormalizedPolygon
from simulation import *

MIN_ECCENTRICITY = 0
MAX_ECCENTRICITY = 0.99
ECCENTRICITY_INC = 0.01

MIN_LENGTH = 0.05
MAX_LENGTH = 2
LENGTH_INC = 0.05

ELLIPSE_SIDES = 100
NUM_TRIALS = 1000

lengths, eccentricities = np.meshgrid(np.arange(MIN_LENGTH, MAX_LENGTH, LENGTH_INC), np.arange(MIN_ECCENTRICITY, MAX_ECCENTRICITY, ECCENTRICITY_INC))
probabilities = []

# for i in range(len(eccentricities)):
#     ellipse = NormalizedPolygon.approximate_ellipse(eccentricities[i][0], ELLIPSE_SIDES)
#     probabilities.append([])
#     for j in range(len(lengths[0])):
#         probabilities[-1].append(buffon_probability(ellipse, lengths[0][j], NUM_TRIALS))

probabilities = [[buffon_probability(ellipse, lengths[0,j], NUM_TRIALS) for j in range(len(lengths[0]))] for ellipse in [NormalizedPolygon.approximate_ellipse(eccentricities[i][0], ELLIPSE_SIDES) for i in range(len(eccentricities))]]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(lengths, eccentricities, np.array(probabilities))
ax.set_xlabel("needle length")
ax.set_ylabel("eccentricity")
ax.set_zlabel("buffon probability")
ax.set_title("Probability on Ellipses by Needle Length")
plt.show()
