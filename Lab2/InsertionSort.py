import sys
import time

def IS(a,length):
    for i in range(1,length,1):
        j = i
        value = a[j]
        while (j > 0 and value < a[j-1]):
            a[j] = a[j-1]
            j = j-1
        a[j] = value

def main():

    filename = "file3"
    length = int(input("How many lines?"))
    a = []
    file = open(filename,"r")
    for i in range(0,length,1):
        a.append(int(file.readline()))

    t1 = time.clock()
    IS(a,length)
    t2 = time.clock()

    print (t2-t1)

main()    
            
                
