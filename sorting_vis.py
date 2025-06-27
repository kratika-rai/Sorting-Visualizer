from tkinter import *
from tkinter import ttk
import random
import time

root=Tk()
root.geometry("700x800")
root.title("Sorting Visualizer")
root.config(bg="#F5F5DC")  


heading = Label(root,text="SORTING VISUALIZER ",font="Arial 20 bold",bg="#F5F5DC",fg="black")
heading.grid(row=0,column=1,padx=20,pady=15)



#functions

def bubble_sort(data,drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j]>data[j+1]:
                data[j], data[j+1]=data[j+1],data[j]
                drawrectangle(data,["#3498db" if x==j or x==j+1 else "#e74c3c" for x in range(len(data))])
                time.sleep(delay)
    drawrectangle(data,["#2ecc71" for x in range(len(data))])
    
def selection_sort(data, drawrectangle, delay):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
            drawrectangle(data, ['#3498db' if x == j or x == min_idx else '#e74c3c' for x in range(len(data))])
            time.sleep(delay)
        
        data[i], data[min_idx] = data[min_idx], data[i]
        drawrectangle(data, ['#3498db' if x == i or x == min_idx else '#e74c3c' for x in range(len(data))])
        time.sleep(delay)

    drawrectangle(data, ['#2ecc71' for _ in range(len(data))])  # Green when sorted

def quick_sort(data, drawrectangle, delay):
    def partition(low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            drawrectangle(data, ['#3498db' if x == j or x == high else '#e74c3c' for x in range(len(data))])
            time.sleep(delay)
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                drawrectangle(data, ['#3498db' if x == i or x == j else '#e74c3c' for x in range(len(data))])
                time.sleep(delay)

        data[i + 1], data[high] = data[high], data[i + 1]
        drawrectangle(data, ['#3498db' if x == i + 1 or x == high else '#e74c3c' for x in range(len(data))])
        time.sleep(delay)
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(data) - 1)
    drawrectangle(data, ['#2ecc71' for _ in range(len(data))])

def merge_sort(data, drawrectangle, delay):
    def merge(left, right, l, r):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        for i in range(len(result)):
            data[l + i] = result[i]
            drawrectangle(data, ['#3498db' if x == l + i else '#e74c3c' for x in range(len(data))])
            time.sleep(delay)

    def divide(l, r):
        if l < r:
            m = (l + r) // 2
            divide(l, m)
            divide(m + 1, r)
            merge(data[l:m + 1], data[m + 1:r + 1], l, r)

    divide(0, len(data) - 1)
    drawrectangle(data, ['#2ecc71' for _ in range(len(data))])


def insertion_sort(data, drawrectangle, delay):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            drawrectangle(data, ['#3498db' if x == j or x == j+1 else '#e74c3c' for x in range(len(data))])
            time.sleep(delay)
        
        data[j + 1] = key
        drawrectangle(data, ['#3498db' if x == j+1 else '#e74c3c' for x in range(len(data))])
        time.sleep(delay)
    
    drawrectangle(data, ['#2ecc71' for _ in range(len(data))])  # Green when sorted


    



def generate_arr():
    global arr
    low=int(lowest_entry.get())
    high=int(highest_entry.get())
    size=int(array_size.get())
    
    arr=[]
    if low > high:
        low, high = high, low  # Swap to ensure valid range

    
    for i in range(size):
        arr.append(random.randrange(low,high+1))
    drawrectangle(arr,['light blue' for x in range(len(arr))])
        

def drawrectangle(arr, colorarray):
    canvas.delete("all")
    canvas_height = 380
    canvas_width = 600
    bar_width = canvas_width/(len(arr)+1)
    border_offset = 30
    spacing = 10
    
    normalized_array = [i /max(arr) for i in arr]  # keeps array in range 0 to 1
    for i,height in enumerate(normalized_array):
        x0=i*bar_width+border_offset+spacing
        y0=canvas_height-height*340
        x1=(i+1)*bar_width+border_offset
        y1=canvas_height
        
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorarray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(arr[i]))
        
        
    root.update_idletasks()
def sorting():
    global arr
    if not arr:
        return
    
    algo = select_algo.get()
    delay = sort_speed.get()

    if algo == "Bubble Sort":
        bubble_sort(arr, drawrectangle, delay)
    elif algo == "Insertion Sort":
        insertion_sort(arr, drawrectangle, delay)
    elif algo == "Selection Sort":
        selection_sort(arr, drawrectangle, delay)
    elif algo == "Merge Sort":
        merge_sort(arr, drawrectangle, delay)
    elif algo == "Quick Sort":
        quick_sort(arr, drawrectangle, delay)


# def sorting():
#     global arr
#     bubble_sort(arr, drawrectangle,sort_speed.get())
    
    
# Blocks
select_algo=StringVar()
# frame 1
f = Frame(root,bg="dark grey",width=500,height=220)
f.grid(row=1,column=1,padx=40,pady=10)

b1=Label(f,text="Algorithm Choice", font="Arial 12", bg="#ecf0f1")
b1.grid(row=0,column=0,padx=10,pady=10)

algmenu = ttk.Combobox(f, textvariable= select_algo , values=['Bubble Sort','Insertion Sort', 'Selection Sort','Merge Sort','Quick Sort'])
algmenu.grid(row=0,column=1,padx=5,pady=5)
algmenu.current(0)


sort_speed = Scale(f, from_=0.1, to=2, length=100, digits=2, resolution=0.1, orient=HORIZONTAL,label="Sorting Speed")
sort_speed.grid(row=0,column=2,padx=5,pady=5)

Button(f,text="Start \nSorting",height=5,width=8, command=sorting).grid(row=0,column=4,padx=5,pady=5)


lowest_entry = Scale(f,from_=1, to=20,resolution=1,orient=HORIZONTAL,label="lowest entry")
lowest_entry.grid(row=1,column=0)

highest_entry = Scale(f,from_=1, to=20,resolution=1,orient=HORIZONTAL,label="highest entry")
highest_entry.grid(row=1,column=1)

array_size = Scale(f,from_=3, to=25,resolution=1,orient=HORIZONTAL,label="Array size")
array_size.grid(row=1,column=2)

Button(f,text="Current\nArray",height=5,width=8,command=generate_arr).grid(row=1,column=4,padx=5,pady=5)


# frame 2
f2 = Frame(root,bg="dark grey",width=800,height=400)


f2.grid(row=2,column=1,padx=40,pady=10)
global canvas
canvas = Canvas(f2,width=600,height=380,bg="white")
canvas.grid(row=0,column=0,pady=5)

root.mainloop() 

