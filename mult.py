import numpy

wid1=5
height1=4
x=numpy.arange(wid1*height1).reshape(wid1,height1)

n=3
y=numpy.arange(n*n).reshape(n,n)

print x

for i in range(wid1-n+1):
    for j in range(height1-n+1):
        print "-------------------------\n",x[i:i+n,j:j+n]
        print numpy.dot(x[i:i+n,j:j+n],y)



