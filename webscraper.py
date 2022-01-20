'''
On the phyphox app, you must connect to a local site. Then, connect the link
to the "URL" in the animate function below. Displays information of the "peaks"
from the sonar data. 
'''


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import find_peaks
from scipy import interpolate
import numpy as np
import numpy.polynomial.polynomial as poly
from bs4 import BeautifulSoup
import requests
# from wood import lines

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_ylim(0, 1)

answer_x = []
answer_y = []

def animate(i):
    global lines, answer_x, answer_y
    URL = "http://192.168.1.151/get?speedofsound&relative_cc=full&distance=full&weighted_cc=full"
    # URL = "http://192.168.1.3/get?speedofsound&relative_cc=full&distance=full&weighted_cc=full"
    r = requests.get(URL).json()
    yar = r['buffer']['relative_cc']['buffer']
    xar = r['buffer']['distance']['buffer'][:len(yar)]
    x_peak = []
    y_peak = []
    
    peaks, _ = find_peaks(yar, prominence = 0.05, distance = 40)
    
    x = np.array(xar)
    y = np.array(yar)
    ax1.clear()
    ax1.plot(xar,yar)
    ax1.plot(x[peaks], y[peaks], 'x')
    
    for num in peaks:
        if x[num] > 90 and y[num] > 0.1:
            print(x[num], y[num])
            x_peak.append(float(x[num]))
            y_peak.append(float(y[num]))
    answer_x += x_peak
    answer_y += y_peak
    # current_closest = [1000]
    # if len(x_peak) == 0:
    #     print("Very low reading or none")
    # else:
    #     for data in lines:
    #         x_val, y_val, material, function = data
    #         final_y = np.polyval(function, x_peak[0])
    #         if current_closest[0] > abs(y_peak[0] - final_y):
    #             current_closest = [abs(y_peak[0] - final_y), y_peak[0], material]
    #         # highest wood
    #         # lowest wall
    #         # if value is above highest wood then classify as high wood
    #         # if value is below lowest wall then classify as low wall 
    #     if current_closest[1] > np.polyval(poly7, x_peak[0]):
    #         print("High Wood")
    #     elif current_closest[1] < np.polyval(poly, x_peak[0]):
    #         print("Low Plaster")
    #     else:
    #         print(current_closest)
            
    
def main():
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
main()
print(answer_x)
print('\n')
print(answer_y)



