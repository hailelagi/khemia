import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# Graph of Open Circuit voltage(y-axis) against Temperature (x-axis)
ocv = np.array([0.0021, 0.0033, 0.0037, 0.00039, 0.00052])
temp = np.array([50, 100, 200, 400, 500])

ocv.sort()
temp.sort()

# smoothen curve
spline = make_interp_spline(temp, ocv)
spline_temp = np.linspace(temp.min(), temp.max())
spline_ocv = spline(spline_temp)

# plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(spline_temp, spline_ocv, '-')

plt.ylabel("Open circuit voltage(v)")
plt.xlabel("Temperature(°C)")
ax.grid()

ax.set_xlim([0, 600])
ax.set_ylim([0, 0.007])

plt.show()
fig.savefig("../images/ocv_vs_temp.png")