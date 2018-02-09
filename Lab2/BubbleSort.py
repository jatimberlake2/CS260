import sys
import time

def BS(a,length):
    for i in range(1,length,1):
        flag = False
        for j in range(i,length,1):
            if (a[j-1] > a[j]):
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
                flag = True
            if flag == False:
                break

def main():

    filename = "file1"
    length = int(input("How many lines?"))
    a = []
    file = open(filename,"r")
    for i in range(0,length,1):
        a.append(int(file.readline()))

    t1 = time.clock()
    BS(a,length)
    t2 = time.clock()

    print (t2-t1)

main()    
            
                
