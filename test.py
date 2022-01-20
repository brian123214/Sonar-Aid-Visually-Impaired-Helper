import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks
from scipy import interpolate

r = csv.reader(open("/Users/briansong/Downloads/Sonar 2020-10-25 11-27-14/Echo location.csv")) 
# r = csv.reader(open("/Users/briansong/Downloads/Sonar 2020-10-25 11-27-57/Echo location.csv"))
lines = list(r)
distance = []
cc = []
for i in range(1, len(lines), 10): 
    a = lines[i][0]
    b = lines[i][1]
    if b == "" or a == "":
        break
    index1 = a.find("E")
    index2 = b.find("E")
    num1 = float(a[:index1])
    num2 = float(b[:index2])
    distance.append(num1 * 10 ** float(a[index1 + 1:]))
    cc.append(num2 * 10 ** float(b[index2 + 1:]))

plt.xlabel("Distance")
plt.ylabel("CC")
plt.plot(distance, cc)

# Smoothing
poly = np.polyfit(distance, cc, 100)
poly_y = np.poly1d(poly)(distance)
plt.plot(distance, poly_y)
y = np.array(poly_y)

x = np.array(distance)
# y = np.array(cc)

peaks, _ = find_peaks(y, prominence = 0.05)
plt.plot(x, y)
plt.plot(x[peaks], y[peaks], 'x')
peaks_x = x[peaks]
peaks_y = y[peaks]
# low = low detection, middle = mid detection, etc.
result = str(len(peaks_x)) + " objects detected. Signals: "

for i in range(len(peaks_x)):
    result += str(round(peaks_x[i]))
    if peaks_y[i] < 0.2:
        result += " low "
    elif 0.2 <peaks_y[i] < 0.4:
        result += " med "
    else:
        result += " high "
    
print(result)



plt.show()

