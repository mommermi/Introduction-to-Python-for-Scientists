import numpy


x = numpy.random.rand(20)*10

y = (0.3*x**3-1.7*x**2-0.7*x-7)*(1+numpy.random.rand(len(x))*0.2-0.1)


data = numpy.transpose([x,y])

numpy.savetxt('data.txt', data, fmt='%7.3f %7.3f')
