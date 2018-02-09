import sys
import time

def SS(a,length):
    for i in range(0,length-1,1):
        minIndex = i
        for j in range(i+1,length,1):
            if (a[j] < a[minIndex]):
                minIndex = j
        temp = a[i]
        a[i] = a[minIndex]
        a[minIndex] = temp

def main():

    filename = "file3"
    length = int(input("How many lines?"))
    a = []
    file = open(filename,"r")
    for i in range(0,length,1):
        a.append(int(file.readline()))

    t1 = time.clock()
    SS(a,length)
    t2 = time.clock()

    print (t2-t1)

main()    
            
                
