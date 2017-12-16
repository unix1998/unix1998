#!  /usr/bin/python
import sys
print "This is the name of the script: ", sys.argv[0]
print "Number of arguments: ", len(sys.argv)
print "The arguments are: " , str(sys.argv)
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 

f(3)
x15 = input ("1 2 3 4 5")
print x15

