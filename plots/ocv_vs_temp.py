import matplotlib.pyplot as plt

# Graph of Open Circuit voltage(y-axis) against Temperature (x-axis)
ocv = [0.0021, 0.0033, 0.0037, 0.00039, 0.00052]
temp = [50, 100, 200, 400, 500]

ocv.sort()
temp.sort()

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(temp, ocv, '.-')

plt.ylabel("Open circuit voltage(v)")
plt.xlabel("Temperature(°C)")

ax.grid()

ax.set_xlim([0, 600])
ax.set_ylim([0, 0.007])

plt.show()

fig.savefig("../images/ocv_vs_temp.png")