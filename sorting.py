import pygame
import random
import time


NUM = 100
WDITH = 800
red_indexs = []
WIN = pygame.display.set_mode((WDITH, WDITH))
pygame.display.set_caption("Sorting Visualiser")


BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)
DARK_GREY = (20,20,20)
LIGHT_GREY = (200,200,200)
RED = (255,0,0)


#<--------------------Draw Screen------------------------->
def draw(array):
    WIN.fill(DARK_GREY)
    draw_bars(array)
    pygame.display.update()

#<--------------------Randomly Generate Array------------------------->
def populate_array(array, num):
    for i in range(num):
        array.append(random.randint(10,WDITH-100))

#<--------------------Draw array to screen------------------------->
def draw_bars(array):
    gap = WDITH//len(array)
    pos = WDITH
    for i in range(len(array)):
        col = LIGHT_GREY
        if array[i] in red_indexs: col = RED
        pygame.draw.rect(WIN, col, (i*gap,WDITH-array[i],gap,array[i]))

#<--------------------Bubble Sort Algorithm------------------------->
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            red_indexs.append(array[j])
            time.sleep(0.0005)
            draw(array)
            red_indexs.remove(array[j])
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

#<--------------------Merge For Merge Sort Algorithm------------------------->
def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):
        time.sleep(0.01)
        draw(array)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1

#<--------------------Merge Sort Algorithm------------------------->
def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)
    


#<--------------------Insertion Sort Algorithm------------------------->
def insertion_sort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            red_indexs.append(arr[j])
            time.sleep(0.008)
            draw(arr)
            arr[j+1] = arr[j] 
            j -= 1
            red_indexs.remove(arr[j+1])
        arr[j+1] = key 
  
#<--------------------Selection Sort Algorithm------------------------->
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        red_indexs.append(arr[i])
        for j in range(i+1, len(arr)-1):
            red_indexs.append(arr[j])
            draw(arr)
            red_indexs.remove(arr[j])
            if arr[j] < arr[min_index]:
                min_index = j
        red_indexs.remove(arr[i])
        arr[i], arr[min_index] = arr[min_index],arr[i]


#<--------------------Heapify For Heap Sort Algorithm------------------------->
def heapify(arr, n, i): 
    time.sleep(0.01)
    draw(arr)
    largest = i 
    l = 2 * i + 1  
    r = 2 * i + 2  
    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # swap 
        heapify(arr, n, largest) 
  
#<--------------------Heap Sort Algorithm------------------------->
def heapSort(arr): 
    n = len(arr) 

    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0) 



#<--------------------Shell Sort Algorithm------------------------->
def shell_sort(array):
    n = len(array)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = array[i]
            j = i
            while j >= gap and array[j-gap]>temp:
                red_indexs.append(array[j])
                time.sleep(0.03)
                draw(array)
                red_indexs.remove(array[j])
                array[j] = array[j-gap]
                j -= gap
            array[j] = temp 
        gap //= 2


#<--------------------Counting Sort ALgorithm For Radix Sort------------------------->
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        time.sleep(0.01)
        draw(array)
        array[i] = output[i]



#<--------------------Radix Sort ALgorithm------------------------->
def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


#<--------------------Bogo Sort Algorithm :)------------------------->
def bogo_sort(array):
    sorted_array = sorted(array)
    go = True
    while sorted_array != array and go:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                go = False
        random.shuffle(array)
        draw(array)

#<--------------------Partition for Quicksort------------------------->
def partition(arr, low, high): 
    i = (low-1)         
    pivot = arr[high]     
    for j in range(low, high): 
        time.sleep(0.008)
        draw(arr)
        if arr[j] <= pivot: 
            i = i+1
            arr[i], arr[j] = arr[j], arr[i] 
            draw(arr)
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    draw(arr)
    return (i+1) 
  

#<--------------------Quicksort Algorithm------------------------->
def quickSort(arr, low, high): 
    draw(arr)
    if len(arr) == 1: 
        return arr 
    if low < high: 
        pi = partition(arr, low, high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 


#<--------------------Main Code------------------------->
def main():
    #create initial array
    set_array = []
    populate_array(set_array, NUM)
    
    run = True

    BubbleSort = False
    MergeSort = True
    InsertionSort = False
    SelectionSort = False
    HeapSort = False
    ShellSort = False
    RadixSort = False
    bogosort = False
    QuickSort = False

    started = False
    while run:
        draw(set_array)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if started:
                continue

            if event.type == pygame.KEYDOWN:
                if event.key ==  pygame.K_SPACE:
                    #run algorithm
                    print(QuickSort)
                    set_array = []
                    populate_array(set_array,NUM)
                    if BubbleSort == True: bubble_sort(set_array)
                    if MergeSort == True:  merge_sort(set_array,0,len(set_array)-1)
                    if InsertionSort == True: insertion_sort(set_array)
                    if SelectionSort == True: selection_sort(set_array)
                    if HeapSort == True: heapSort(set_array)
                    if ShellSort == True: shell_sort(set_array)
                    if RadixSort == True: radixSort(set_array)
                    if bogosort == True: bogo_sort(set_array)
                    if QuickSort == True: quickSort(set_array,0,len(set_array)-1)
                
                if event.key == pygame.K_c:
                    #reset array
                    set_array = []
                    populate_array(set_array,NUM)
                if event.key == pygame.K_b:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    BubbleSort = True

                if event.key == pygame.K_m:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    Radix_Sort = False
                    bogosort = False
                    QuickSort = False
                    MergeSort = True

                if event.key == pygame.K_i:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    InsertionSort = True

                if event.key == pygame.K_s:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    SelectionSort = True

                if event.key == pygame.K_h:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    HeapSort = True

                if event.key == pygame.K_l:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    ShellSort = True

                if event.key == pygame.K_r:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    RadixSort = True

                if event.key == pygame.K_g:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    bogosort = True

                if event.key == pygame.K_q:
                    MergeSort = False
                    BubbleSort = False
                    InsertionSort = False
                    SelectionSort = False
                    HeapSort = False
                    ShellSort = False
                    RadixSort = False
                    bogosort = False
                    QuickSort = False
                    QuickSort = True
  
main()