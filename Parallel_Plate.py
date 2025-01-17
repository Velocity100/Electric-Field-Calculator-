import numpy as np
from ElibV3 import E2d
#positions
x1 = np.arange(-1,1,0.05)
y1 = np.ones_like(x1)*-0.5
q1 = np.ones_like(x1)
x2 = np.arange(-1,1,0.05)
y2 = np.ones_like(x1)*0.5
q2 = np.ones_like(x1)*-1
q,xpos,ypos = np.append(q1,q2),np.append(x1,x2),np.append(y1,y2)
#make grid
u = np.arange(-3,3,0.3)
x,y = np.meshgrid(u,u)
#E field
Ex,Ey = E2d(x,y,q,xpos,ypos)[:2]
#reshape E field for matplotlib
Ex,Ey = Ex.reshape(x.shape),Ey.reshape(y.shape)
#plot 2d vector field
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
colors = np.log(np.sqrt(Ex**2 + Ey**2))
ax.streamplot(x, y, Ex,Ey,density=2.5,color=colors,cmap=plt.cm.plasma)
for i in range(len(xpos)):
        if q[i] > 0: 
            ax.plot(xpos[i],ypos[i],marker='o',c="#4CC9F0")
        else:
            ax.plot(xpos[i],ypos[i],marker='o',c="#F72585")
plt.show()