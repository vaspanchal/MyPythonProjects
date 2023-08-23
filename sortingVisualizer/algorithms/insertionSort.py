import time
from colors import *

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >=0 and key < data[j]:
            data[j+1] = data[j]
            j = j-1

        data[j+1] = key
        drawData(data, [LIME if x == j or x < i else LIGHT_GRAY for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])




