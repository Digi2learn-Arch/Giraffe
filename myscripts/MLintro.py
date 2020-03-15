

import numpy
from scipy import stats
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

print('\nMean : ')
print(numpy.mean(speed))

print('\nMedian : ')
print( numpy.median(speed))

print('\nMode : ')
print(stats.mode(speed))

print('\nSTD : ')
print(numpy.std(speed))

print('\nVariance : ')
print(numpy.var(speed))

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

print('\nPercentile : ')
print(numpy.percentile(ages, 75))


x = numpy.random.normal(5, 1, 10) # normal(mean, sd, no of values)

x.sort()

print('\n')
print(x)

plt.hist(x, 100)
#plt.hist(x, 50)


print('\n')
print(numpy.mean(x))
print(numpy.std(x))


plt.show()



x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()