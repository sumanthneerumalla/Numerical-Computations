# test_polyfit.py     polyfit in Python, needs numpy
from numpy import array
from numpy import polyfit
from numpy import polyval
import math


# on known polynomial first
print "fitting to data from thrust chart approximation"
xx = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
yy = [0,5.5,12,5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,0] 

for i in range(3,18):
    print "n = ", i

    p=polyfit(xx,yy,i)
    yy1=polyval(p,xx)
    
    err=abs(yy-yy1)    

    maxError = max(abs(yy - yy1))
    print "maximum error is: ", maxError

    sumerr=sum(err)

    avgError= sumerr/len(yy)
    print "Average error is: ", avgError

    rms = math.sqrt(sumerr**2/len(yy)) #used formula for rms 
    print "RMS is: ",rms

    print ""
