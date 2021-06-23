# Graph of power density(y-axis) against current density(x-axis)

import matplotlib.pyplot as plt

power_density = [0.047, 0.051, 0.067, 0.052, 0.055]
current_density = [0.031, 0.038, 0.057, 0.061, 0.083]

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(current_density, power_density, '.-')

plt.ylabel("Power Density (mW/cm2))")
plt.xlabel("Current Density (mA/cm2)")

ax.grid()

plt.show()

fig.savefig("../images/power_vs_current_density.png")
