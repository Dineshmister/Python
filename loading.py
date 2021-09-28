#To await the loop time module is imported
import time

def loading():
    # initialising variable i to 1
    i = 0

    #setting loop limit to 101 so we get 100 as last value
    while(i<101):

     #carriage return is used to print the values in one on top of one and end will restrict the loop to next line
     print("\rLoading...",i,end="%")

     #when one value is printed it will wait for 0.1 sec to go for loop
     time.sleep(0.1)

     #incrementing i value
     i+=1
     #when the loop is fully excecuted it will wait for .4sec and finally it will print completed
    time.sleep(.4)
    print("\rCompleted")
#calling function
loading()

