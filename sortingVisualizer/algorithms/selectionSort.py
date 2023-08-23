import time
from colors import *

def selection_sort(data,drawData,timeTick):
    n = len(data)
    for i in range(n): #to run n-1 passes
        minIndex = i
        for j in range(i+1,n):
            if data[j] < data[minIndex]:
                minIndex = j

        data[i],data[minIndex] = data[minIndex], data[i]
        drawData(data, [LIME if x == minIndex or x < i else LIGHT_GRAY for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])

