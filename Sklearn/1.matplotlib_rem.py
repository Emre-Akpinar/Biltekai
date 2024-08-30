import matplotlib.pyplot as plt
import numpy as np

x = np.arange(10)
y = [y for y in range(10)]

plt.plot(x,y)
plt.xlabel("x's")
plt.ylabel("y's")

plt.show()

plt.scatter(x,y,lw=.01,marker='*',color='red')
plt.show()


