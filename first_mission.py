import matplotlib.pyplot as plt
import matplotlib.animation as animation
yaxis=[20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
xaxis=[i for i in range(0,len(yaxis))]
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
i=0
def quicksho(arr):
    global i,yaxis
    i=i+1
    key=yaxis[i]
    j=i-1
    while j>=0 and yaxis[j]>key and i<len(yaxis):
        yaxis[j+1]=yaxis[j]
        j=j-1
    yaxis[j+1]=key
    ax1.clear()
    ax1.plot(xaxis,yaxis)
    print(yaxis)
ani=animation.FuncAnimation(fig,quicksho,interval=10)
plt.show()
print(yaxis)


#for bar graphimport matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
yaxis=[20,1,17,3,2,8,6,5,9,19,18,13,22,14,15,5,2,7,6]
xaxis=[i for i in range(0,len(yaxis))]
pos=np.arange(len(yaxis))+0.0001
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
i=0
def quicksho(arr):
    global i,yaxis
    i=i+1
    key=yaxis[i]
    j=i-1
    while j>=0 and yaxis[j]>key and i<len(yaxis):
        yaxis[j+1]=yaxis[j]
        j=j-1
    yaxis[j+1]=key
    ax1.clear()
    plt.bar(pos,yaxis)
    print(yaxis)
ani=animation.FuncAnimation(fig,quicksho,interval=10)
plt.show()
print(yaxis)





















