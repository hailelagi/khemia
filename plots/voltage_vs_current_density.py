import matplotlib.pyplot as plt

# Graph of cell voltage(y-axis) against current density(x-axis)

ocv = [0.0021, 0.0033, 0.0037, 0.00039, 0.00052]
current_density = [0.031, 0.038, 0.057, 0.061, 0.083]

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(current_density, ocv, '.-')

plt.ylabel("Open circuit voltage(v)")
plt.xlabel("Current Density (mA/cm2)")

ax.grid()
plt.show()

fig.savefig("../images/voltage_current_density.png")