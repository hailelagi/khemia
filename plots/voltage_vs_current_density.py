import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, interp1d

# Graph of cell voltage(y-axis) against current density(x-axis)

ocv = np.array([0.0021, 0.0033, 0.0037, 0.00039, 0.00052])
current_density = np.array([0.031, 0.038, 0.057, 0.061, 0.083])

# smoothen curve
spline = make_interp_spline(sorted(current_density), sorted(ocv))
spline_current_density = np.linspace(min(current_density), max(current_density))
spline_ocv = spline(spline_current_density)

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot(spline_current_density, spline_ocv, '-')

plt.ylabel("Open circuit voltage(v)")
plt.xlabel("Current Density (mA/cm2)")

ax.grid()
plt.show()

fig.savefig("../images/voltage_current_density.png")