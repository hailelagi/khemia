import matplotlib.pyplot as plt

# Graph of cell voltage(y-axis) against power density(x-axis) at 500 C

ocv = [0.0021, 0.0033, 0.0037, 0.00039, 0.00052]
power_density = [0.047, 0.051, 0.067, 0.052, 0.055]

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(power_density, ocv, '.-')

plt.ylabel("Open circuit voltage(v)")
plt.xlabel("Power Density (mW/cm2))")

ax.grid()
plt.show()

fig.savefig("../images/voltage_power_density.png")