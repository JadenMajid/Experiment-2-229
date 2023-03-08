import matplotlib.pyplot as plt
import numpy as np


fname = 'AveragedData.csv'
# the data file fname has x data (first column) and y data (second column) and
# the uncertianty in y (third column).
# Enter the name and units of each column here so that the plots are properly
# labeled. e.g. x_name = 'Time', x_units = 'ms', y_name = 'Voltage', y_units
# = 'V'.
x_name = 'Frequency'
x_units = 'Hz'
y_name = 'Vout/Vin'
y_units = 'no units'

titles = ("Temperature over time for rough rod while cooling",
          "Temperature over time for polished rod while cooling",
          "Temperature over time for lacquered rod while cooling")

colours = ["r.", "g.", "b."]

data = np.loadtxt(fname, delimiter=',', comments='#',
                  usecols=(0, 1))
# access the data columns and assign variables x,y  and  uncetainty in y y_sigma
x = data[:, 0]
y = data[:, 1]

plt.figure(2)
plt.plot(x, y)
plt.title("Temperature over time for all 3 rods")
plt.legend(["Rough", "Polished", "Lacquered"])
plt.xlabel("Time(s)")
plt.ylabel("Temperature(K)")
plt.show()
