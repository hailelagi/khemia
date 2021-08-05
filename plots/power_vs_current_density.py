import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Graph of power density(y-axis) against current density(x-axis)

power_density = np.array([0.047, 0.051, 0.067, 0.052, 0.055])
current_density = np.array([0.031, 0.038, 0.057, 0.061, 0.083])

# smoothen curve
spline = make_interp_spline(current_density, power_density)
spline_current_density = np.linspace(current_density.min(), current_density.max(), 5000)
spline_power_density = spline(spline_current_density)

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(spline_current_density, spline_power_density, '-')

plt.ylabel("Power Density (mW/cm2)")
plt.xlabel("Current Density (mA/cm2)")

ax.grid()
plt.show()

fig.savefig("../images/power_vs_current_density.png")
