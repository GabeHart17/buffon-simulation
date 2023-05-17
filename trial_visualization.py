from polygon import NormalizedPolygon
from simulation import *
import matplotlib.pyplot as plt
import matplotlib.lines as lines

ECCENTRICITY = 0.8
NUM_SIDES = 100

NUM_TRIALS = 50
NEEDLE_SIZE = 0.1

ellipse = NormalizedPolygon.approximate_ellipse(ECCENTRICITY, NUM_SIDES)

ellipse_x = [v[0] for v in ellipse.vertices] + [ellipse.vertices[0][0]]  # add the first coordinate again so last segment is rendered
ellipse_y = [v[1] for v in ellipse.vertices] + [ellipse.vertices[0][1]]

max_extent = max(ellipse_x + ellipse_y) * 1.10  # 10% margin for ease of visualization

ellipse_line = lines.Line2D(ellipse_x, ellipse_y)

trial_results = [buffon_trial(ellipse, NEEDLE_SIZE) for i in range(NUM_TRIALS)]
needle_lines = [lines.Line2D([x[0], y[0]], [x[1], y[1]], color='g' if success else 'r') for success,x,y in trial_results]

fig, ax = plt.subplots()
ax.add_line(ellipse_line)
for line in needle_lines:
    ax.add_line(line)
ax.set_xlim(-max_extent, max_extent)
ax.set_ylim(-max_extent, max_extent)
plt.show()
