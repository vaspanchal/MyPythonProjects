import time
from colors import *

def bubble_sort(data, drawData, timeTick):
    n = len(data)
    for i in range(n-1): #no of passes
        for j in range(n - i - 1): #no of steps in each pass
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                drawData(data, [LIME if x==j or x==j+1 or x>j else LIGHT_GRAY for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])



