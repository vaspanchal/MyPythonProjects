from tkinter import *
from tkinter import ttk
import random
from colors import *
from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.selectionSort import selection_sort
from algorithms.insertionSort import insertion_sort

#main window
window = Tk()
window.title("Sorting Visualizer")
window.maxsize(825,530) #default 1000x700
window.config(bg= BLACK)

algo_name = StringVar() #it holds string data
algo_list = ['Selection Sort','Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'] #sorting algos

algo_speed = StringVar()
speed_list = ['Fast','Medium','Slow']

data = [] #this will be filled by random values



def generate(): #it will generate random array
    global data

    data = []
    for i in range(0,100):
        rand = random.randint(1,150)
        data.append(rand)

    drawData(data, [LIGHT_GRAY for x in range(len(data))])

def drawData(data, colorArray): #to draw vertical bars from randomly generated data
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2 # it is also changing bar width
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i+1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0,y0,x1,y1,fill = colorArray[i])

    window.update()
def set_speed(): #to set sroting speed
    if speed_menu.get() == 'Slow':
        return 0.1
    elif speed_menu.get() == 'Medium':
        return 0.01
    else:
        return 0.000001

def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)

    elif algo_menu.get() == 'Selection Sort':
        selection_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Insertion Sort':
        insertion_sort(data, drawData, timeTick)

    else:
        pass



#for user interface

frm = Frame(window, width=900, height=300, bg=BLACK)
frm.grid(row=0,column=0,padx=10,pady=5)

#dropdown for algo selection
cb1 = Label(frm, text='Algorithm:', bg=WHITE)
cb1.grid(row=0,column=0, padx=10,pady=5)
algo_menu = ttk.Combobox(frm, textvariable=algo_name, values=algo_list)
algo_menu.set("-select-")
algo_menu.grid(row=0,column=1,padx=5,pady=5)
#algo_menu.current(0) #current shows default value in combobox and 0 is index of that value from list

#dropdown for sorting speed
cb2 = Label(frm, text='Sorting Speed:', bg=WHITE)
cb2.grid(row=1,column=0, padx=10,pady=5)
speed_menu = ttk.Combobox(frm, textvariable=algo_speed, values=speed_list)
speed_menu.set("-select-")
speed_menu.grid(row=1,column=1,padx=5,pady=5)
#speed_menu.current(0)

#button to sort
b1 = Button(frm, text='sort', command=sort,bg=LIME)
b1.grid(row=2,column=1, pady=5, padx=5)

#button to generate random array
b2 = Button(frm,text = 'generate array', command=generate, bg=LIME)
b2.grid(row=2,column=0, padx=5, pady=5)


#canvas to draw array
canvas = Canvas(window, width=800, height=400, bg=BLACK)
canvas.grid(row=1, column=0, padx=10, pady=5)




window.mainloop()
