import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, interp1d

# Graph of cell voltage(y-axis) against power density(x-axis) at 500 C

ocv = np.array([0.0021, 0.0033, 0.0037, 0.00039, 0.00052])
power_density = np.array([0.047, 0.051, 0.067, 0.052, 0.055])

# smoothen curve
spline = make_interp_spline(sorted(power_density), sorted(ocv))
spline_power_density = np.linspace(min(power_density), max(power_density))
spline_ocv = spline(spline_power_density)

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(spline_power_density, spline_ocv, '-')

plt.ylabel("Open circuit voltage(v)")
plt.xlabel("Power Density (mW/cm2)")

ax.grid()
plt.show()

fig.savefig("../images/voltage_power_density.png")