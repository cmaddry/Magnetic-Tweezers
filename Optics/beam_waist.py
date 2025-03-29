import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from scipy.special import erf

## Functions
# Function for plotting
def f(x):
    return 0.5*(1+erf((-hx0+x)*np.sqrt(2)/hw))

# Function for fitting
def func(x, hx0, hw):
    return 0.5*(1+erf((-hx0 + x)*np.sqrt(2)/hw))



## Short Distance Low Power
# Data from the experiment
x_distance = [0, 0.4, 0.8, 1.2, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.2, 3.6]
laser_power = [0.106, 0.156, 0.217, 0.333, 1.103, 3.69, 15.3, 26.9, 35.0, 39.3, 39.9, 40.2, 40.3]

# Normalize the vector to the max power
laser_power_array = np.array(laser_power)/40.3

# Fitting the data
fit, error = curve_fit(func, x_distance, laser_power_array, bounds=(0, [3.6, 2]))
hx0 = fit[0]
hw = fit[1]
print(f"Beam waist: {hw:.4f} mm")

# Plotting the fit
plt.scatter(x_distance, laser_power_array, color = "#009900", zorder = 1)
plt.plot(x_distance, f(np.array(x_distance)), color = "#ff5050", label=f"Fit with width = {hw:.2f} and hx0 = {hx0:.2f}", zorder = 0)
plt.title("Short Distance Low Power"); plt.xlabel("Distance (mm)"); plt.ylabel("SLED Power (uW)")
plt.legend()
plt.show()



## Short Distance High Power
x_distance = [0, 0.4, 0.8, 1.0,  1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8]
laser_power = [0.863, 0.861, 0.855, 0.843, 0.747, 0.575, 0.316, 0.0762, 0.0225, 6/1000, 3.66/1000, 2.20/1000, 1.278/1000]

# Normalize the vector to the max power
laser_power_array = np.array(laser_power)/0.863

# Fitting the data
fit, error = curve_fit(func, -np.array(x_distance) + 2.8, laser_power_array, bounds=(0, [3.6, 2]))
hx0 = fit[0]
hw = fit[1]
print(f"Beam waist: {hw:.4f} mm")

# Plotting the fit
plt.scatter(np.array(x_distance), laser_power_array, color = "#009900", zorder = 1)
plt.plot(-np.array(x_distance) + 2.8, f(np.array(x_distance)), color = "#ff5050", label=f"Fit with width = {hw:.2f} and hx0 = {hx0:.2f}", zorder = 0)
plt.title("Short Distance High Power"); plt.xlabel("Distance (mm)"); plt.ylabel("SLED Power (mW)")
plt.legend()
plt.show()



## Long Distance Low Power
x_distance = [0, 0.4, 0.8, 1.0,  1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.2, 3.6, 4.0, 4.4, 4.8]
laser_power = [1.62, 3.15, 8.57, 13.9, 18.7, 25.0, 30.6, 34.3, 36.6, 37.8, 38.3, 38.6, 38.7, 39.0, 39.2, 39.3, 39.9, 39.9]

# Normalize the vector to the max power
laser_power_array = np.array(laser_power)/39.9

# Fitting the data
fit, error = curve_fit(func, x_distance, laser_power_array, bounds=(0, [3.6, 2]))
hx0 = fit[0]
hw = fit[1]
print(f"Beam waist: {hw:.4f} mm")

# Plotting the fit
plt.scatter(x_distance, laser_power_array, color = "#009900", zorder = 1)
plt.plot(x_distance, f(np.array(x_distance)), color = "#ff5050", label=f"Fit with width = {hw:.2f} and hx0 = {hx0:.2f}", zorder = 0)
plt.title("Long Distance Low Power"); plt.xlabel("Distance (mm)"); plt.ylabel("SLED Power (uW)")
plt.legend()
plt.show()



## Long Distance High Power
x_distance = [0, 0.4, 0.8, 1.2, 1.6, 2.0, 2.4, 2.8, 3.2, 3.6, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4]
laser_power = [0.854, 0.854, 0.853, 0.853, 0.852, 0.851, 0.850, 0.847, 0.843, 0.837, 0.829, 0.817, 0.788, 0.728, 0.639, 0.512, 0.380, 0.249, 0.153, 0.0909, 60.9/1000, 44.2/1000, 33.3/1000]

# Normalize the vector to the max power
laser_power_array = np.array(laser_power)/0.854

# Fitting the data
fit, error = curve_fit(func, -np.array(x_distance) + 6.4, laser_power_array, bounds=(0, [3.6, 2]))
hx0 = fit[0]
hw = fit[1]
print(f"Beam waist: {hw:.4f} mm")

# Plotting the fit
plt.scatter(x_distance, laser_power_array, color = "#009900", zorder = 1)
plt.plot(-np.array(x_distance) + 6.4, f(np.array(x_distance)), color = "#ff5050", label=f"Fit with width = {hw:.2f} and hx0 = {hx0:.2f}", zorder = 0)
plt.title("Long Distance High Power"); plt.xlabel("Distance (mm)"); plt.ylabel("SLED Power (mW)")
plt.legend()
plt.show()