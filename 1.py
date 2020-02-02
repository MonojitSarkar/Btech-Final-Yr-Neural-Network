import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3]
y = [1,2,3]
#y = mx+c Considering intercept to be 0
#theta1 = [-2,-1.5,-1,-0.5,0,1.0,1.5,1.6,1.7,1.8,1.9,2]
theta1 = np.linspace(-2,2,20)
print(theta1)
#y1 = [i*theta1 for i in x]


def costAvg(theta1,y,x):
    cost = []
    for a in theta1:
        y1 = [i*a for i in x]
        print(y1)
        for b,c in zip(y1,y):
            sum = 0
            sum = sum + (b-c)**2
            print(sum)
        avg = sum/(2*3)
        cost.append(avg)
    return cost

costs = costAvg(theta1,y,x)
print(costs)
plt.plot(theta1,costs,'*')
plt.show()
