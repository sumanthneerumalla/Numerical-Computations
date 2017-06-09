# lsfit_lect.c  from lecture notes    needs numpy
#               run  python lsfit_lect.py > lsfit_lect_py.out

from numpy import array
from numpy.linalg import solve

print "lsfit_lect.py run to make lsfit_lect_py.out "


time = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]

thrust = [0,5.5,12,5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,4.5,0]


xd=array([[1.0, 2.5, 3.7],
          [2.0, 2.5, 3.6],
          [3.0, 2.7, 3.5],
          [2.2, 2.1, 3.1],
          [1.5, 2.0, 2.6],
          [1.6, 2.0, 3.1]])
A=array([[0.0 for j in range(3)] for i in range(3)])
X=array([0.0 for i in range(3)])
Y=array([0.0 for i in range(3)])   # |A| * |X| = |Y|  |X| will be  a, b, c

print "xd="
print  xd
yd=array([32.5, 7.2, 6.9, 22.4, 10.4, 11.3])
print "yd="
print yd

for i in range(3):
  Y[i] = 0.0 # must start sum with zero
  for k in range(6):
    Y[i] = Y[i] + xd[k][i]*yd[k] # Xi * Yk

  for j in range(3):
    A[i][j] = 0.0   # must start sum with zero
    for k in range(6): # run through observations
        A[i][j] = A[i][j] + xd[k][j]*xd[k][i]  #  Xj * Xi


X = solve(A, Y)
print "a b c="
print X

# check
print "really bad fit"
for k in range(6):  # k is observation
  print "Y_actual=",
  print yd[k],
  print "  Y_approximate=",
  print X[0]*xd[k][0]+X[1]*xd[k][1]+X[2]*xd[k][2]

# end lsfit_lect.py
