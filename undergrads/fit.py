import numpy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

######### introduction

print 'hello world'

# functions
def add(a,b):
    return a+b

print add(1,2)

# lists
a = [3,4,5,6,7]

# numpy arrays
b = numpy.array(a)
c = numpy.arange(0, 5, 1)

print b-c
print b-3



######### exercise: data fitting

def func(x, a, b, c, d):
    return a*x*x*x + b*x*x + c*x + d


### read in data
data = numpy.genfromtxt('data.txt', dtype=[('x', float), ('y', float)])

### fit function
popt, pcov = curve_fit(func, data['x'], data['y'])

print popt

### plot data

f, (ax1,ax2) = plt.subplots(1,2)

ax1.scatter(data['x'], data['y'])
x = numpy.arange(0, 10, 0.1)
ax1.plot(x, func(x, *popt), color='red')
ax1.set_xlabel('x')
ax1.set_ylabel('y')


ax2.set_xlabel('delta y')
ax2.set_ylabel('frequency')
ax2.hist(data['y']-func(data['x'], *popt))

plt.show()



