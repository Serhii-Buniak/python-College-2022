from numpy import *
import matplotlib.pyplot as plt
x = linspace(0, 3, 51)
y1 = x**(1/2)*sin(10*x)
plt.plot(x, y1, label='x^(1/2)*sin(10*x)')
plt.plot(x, y1, label='x^(1/2)*sin(10*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plotting two curves in the same plot')
plt.legend()
plt.show()