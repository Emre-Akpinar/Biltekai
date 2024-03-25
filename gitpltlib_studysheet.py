import matplotlib.pyplot as plt
import numpy as np

'''
X_data = np.random.random(100)*100
Y_data = np.random.random(100)*100
"""
X_data = [x for x in range(100)]
Y_data = [y for y in range(100)]
""" 
#           xcoord ycoord size  what       color     transparency
plt.scatter(X_data,Y_data,s=150,marker="*",c="green",alpha=0.3) #write scatter for dotted graph
plt.show()
'''

"""
years = [2019 + x for x in range(5)]
weights = [98,92,81,76,73]

plt.plot(years, weights, color="r", lw=2, marker="*", linestyle="--") # the default is lines so dont need to write lines or smth just plot
plt.plot(years, weights, "r--", lw=2, marker="*")#same 
plt.show()
"""

"""
ProLan = ["C","C#","Python","Java","Go"]
votes = [20,40,150,5,30]

plt.bar(ProLan, votes, color="b", edgecolor="black",lw=3 )
plt.show
"""

"""
ages = np.random.normal(20, 1.5 ,1000)

plt.hist(ages,bins=125,''''cumulative=True''')#cumulative shows how many people at that age or below
plt.show()
"""

"""
ProLan = ["Python", "C", "C#", "Java", "Go"]
votes = [50,24,14,6,17]
explodes = [0,0,0,0,0]

plt.pie(votes, labels=ProLan, explode=explodes, autopct="%.2f%%",
        pctdistance=0.8, startangle=90)
plt.show()
"""

'''
heights = np.random.normal(172,8,300)
plt.boxplot(heights)
plst.show( )
'''

"""
first = np.linspace(0,10,25)
second = np.linspace(10,200,25)
third = np.linspace(200,210,25)
fourth = np.linspace(210,230,25)

data = np.concatenate((first,second,third,fourth))

plt.boxplot(data)
plt.show()
"""

# Costumazation

"""
years = [2014 + x for x in range(8)]
income = [55, 56, 62, 61, 72, 72, 73, 75]

income_ticks = list(range(50,81,2))

plt.plot(years, income)
plt.title("Income of Emre", color="g", fontsize=16, fontname="Aerial")
plt.xlabel("Year")
plt.ylabel("Yearly Income in USD")
plt.yticks(income_ticks,[f"${x}k" for x in income_ticks])
plt.show()
"""

# Legends and Multiple plots

"""
#plot
stock_a = [100,102,99,101,101,100,102]
stock_b = [90,95,102,104,105,103,109]
stock_c = [110,115,100,105,100,98,95]
stock_d = [95,94,96,100,110,140,200]

plt.plot(stock_a, label="Company a")
plt.plot(stock_b, label="Company b") # İf i only give one argument its gonna be y value and x is generated automatically
plt.plot(stock_c, label="Company c")
plt.plot(stock_d, label="Nvidia")
plt.legend(loc="upper center")  # puts the labels on the plot 
plt.show()
"""

"""
#piechart

votes = [10, 2, 5, 16, 22]
people = ["A", "B", "C", "D", "E"]

plt.pie(votes, labels=None)
plt.legend(labels=people)
plt.show
"""

# Plot styling

"""
from matplotlib import style

pilots = ["Hamilton", "Verstappen", "Alonso", "Leclerc", "Sainz"]
votes = [150,100,50,80,70]

style.use("dark_background")

plt.pie(votes,labels=None)
plt.legend(pilots,loc="upper left")
plt.show()
"""

# Multiple plots
"""
x1, y1 = np.random.random(100), np.random.random(100)
x2, y2 = np.arange(100), np.random.random(100)

plt.figure(1)
plt.scatter(x1, y1)

plt.figure(2)
plt.plot(x2, y2)

plt.pie(x1, y1)


plt.show()
"""

#
"""
x = [0]
a=0
for i in range(500):
    a+=0.2
    x.append(a)
plt.plot(x, np.sin(x))
plt.show()
"""
#


# Subplots
"""


from matplotlib import style


style.use("dark_background")

x = [0]
a=0
for i in range(500):
    a+=0.2
    x.append(a)



pilots = ["Hamilton", "Verstappen", "Alonso", "Leclerc", "Sainz"]
votes = [150,100,50,80,70]

x_data, y_data = np.random.random(100), np.random.random(100)
x = np.arange(100) 


fig, axs = plt.subplots(2, 2)

fig.suptitle("Four Plots")



axs[0,0].plot(x, y_data)
axs[0,0].set_title("Random Func")

axs[0,1].scatter(x_data, y_data)
axs[0,1].set_title("Random Scatter")

axs[1,0].pie(votes,labels=pilots)
axs[1,0].set_title("Pilots fans")

axs[1,1].plot(x, np.sin(x))
axs[1,1].set_title("Sine Func")

plt.show()

#Exporting plots 
plt.savefig("fourplots.png", dpi=300)
"""

# 3d plotting
"""
ax = plt.axes(projection="3d")

x = np.arange(0,100,0.1)
y = np.sin(x)
z = np.cos(x)

ax.plot(x, y, z,lw=3)
ax.set_title("3D Plotting")

ax.set_xlabel("Random Num")
ax.set_ylabel("sin(x)")
ax.set_zlabel("cos(x)")

plt.show()
"""

# Animating Plots
import random

"""
heads_tails = [0,0]

for _ in range(1000):
    x = random.randint(0,1)
    heads_tails[x] += 1
    plt.bar(["Heads", "Tails"],heads_tails,color=["red","black"])
    plt.show()    
"""

"""
x = []
y = []
a = 0

for _ in range(100):
    a += 1
    x.append(a)
    b = np.random.normal(99)
    y.append(b)
    plt.plot(x, y)
    plt.title("Stock Market")
    plt.xlabel("Days")
    plt.ylabel("USD per stock")
    plt.show()
"""


from mpl_toolkits.mplot3d import Axes3D
"""
ax = plt.axes(projection="3d")

x = np.arange(0,100,0.1)
y = np.sin(x)
z = np.cos(x)


ax.plot(x, y, z)
ax.view_init(elev=75, azim=60)  # Example values for elevation and azimuth elevation:vertical, azimuth:horizontal
plt.show()
"""

"""
def is_prime(n):
    flag = 0
    for i in range(int(n/2)+1):
        if i == 0 or i == 1:
            continue
        else:
            if n % i == 0:
                flag = 1

    if flag == 1:
        return False
    else:
        return True

from math import sqrt
ax = plt.axes(projection="3d")

primes = [sqrt(i) for i in range(10000) if is_prime(i)]
x = np.sin(primes)
z = np.cos(primes)

ax.plot(x, primes, z)
plt.show()
plt.savefig("3dplot.png")
"""


























