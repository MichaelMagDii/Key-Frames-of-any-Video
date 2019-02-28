import cv2
import numpy as np
import os


def getKey(img):
    return len(img)


#sort function
def bubble_sort(lst, asc=True):
    lst = list(lst)  # copy collection to list
    for passesLeft in range(len(lst)-1, 0, -1):
        for i in range(passesLeft):
            if asc:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            else:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


#we will make concatenation by other words in some kind of array ('abuse')
dir = #Link of Video or Upload any video to read it
list = os.listdir(dir) # dir is your directory path
number_files = len(list)
#print (number_files)
numofframes = number_files - 1
#print (numofframes)
# to intialize first value


arr = []
for i in range(0,numofframes-1):
    name1 = #any location on your pc to Save a fame.Jpg
    name2 = #any location on your pc to Save a fame.Jpg
    img1 = cv2.imread(name1)
    img2 = cv2.imread(name2)
    img = cv2.absdiff(img2, img1)#subtract two images
    arr.append(img)
    i = i + 1
    
#sort every subtracted image
arr = sorted(arr, reverse=True, key=getKey)
for i in range(0,3):
    cv2.imshow('image ' + str(i), arr[i])


