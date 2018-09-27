''' 
mytimer.py- a program to test the speed of your computer
oliver.tattersall - original coding, sept. 21, 2018
'''




# import timeit module
#only import the required function - it speeds up your code
from timeit import default_timer as timer

#defining the function callded mytimer
def mytimer():
    #everything that is idented below is part of the function
    start=timer()
    print(start)
	
    for i in range(1000000):
		print(i)
		
    end=timer()
    print(end)
	
    print(end-start)

#this is the actually call of the function	
mytimer()