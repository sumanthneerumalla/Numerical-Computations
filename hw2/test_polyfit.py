# test_polyfit.py     polyfit in Python, needs numpy
from numpy import array
from numpy import polyfit
from numpy import polyval


def f(x):
  return 5.0 + 4.0*x + 3.0*x*x + 2.0*x*x*x + 1.0*x*x*x*x

print "test_polyfit.py  a x,y,5) "

# on known polynomial first
print "fit 5.0 + 4.0*x + 3.0*x*x + 2.0*x*x*x + 1.0*x*x*x*x"
xx = [0.0 for i in range(5)]
yy = [0.0 for i in range(5)]

for i in range(5):
  xx[i] = 0.1*(i+1)
  yy[i] = f(xx[i])
  print "i=",
  print i,
  print " ,xx=",
  print xx[i],
  print " ,yy=",
  print yy[i]

print "p=polyfit(xx,yy,4) for 5 points"
p=polyfit(xx,yy,4) # 5 input values, 4th order
print "polyfit coefficients"
print p
print "backwards? largest power first, expected 5, 4, 3, 2, 1"
print " "
print "polyval values of fit"
yy1=polyval(p,xx)
print yy1
print "should be values above"
print " "

x=array([0.0, 0.1,  0.2, 0.3, 0.4, 1.8, 1.9])
print "x="
print  x
y=array([0.0, 6.0, 14.1, 5.5, 4.5, 4.5, 0.0])
print "y="
print y

p=polyfit(x,y,5)
print "polyfit p=polyfit(x,y,5)"
print p

# polyval
y1=polyval(p,x)
print "polyval y1=polyval(p,x)"
print y1

err=abs(y-y1)
print "err=abs(y-y1) an array",
print err

sumerr=sum(err)
print "sumerr=sum(err) a number",
print sumerr

