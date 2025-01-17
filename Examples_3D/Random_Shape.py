import numpy as np
from ElibV3 import E3d
#positions and charges
t = np.arange(0,2*np.pi,2*np.pi/1000)
x1 = np.cos(t)**5
y1 = np.sin(t)**5
z1 = np.ones_like(x1)*-1/2
q1 = np.ones_like(x1)*-1

x2 = np.cos(t)**5
y2 = np.sin(t)**5
z2 = np.ones_like(x2)*1/2
q2 = np.ones_like(x2)

xpos,ypos,zpos,q = np.append(x1,x2),np.append(y1,y2),np.append(z1,z2),np.append(q1,q2)

#make grid
u = np.linspace(-1.5,1.5,20)
x,y,z = np.meshgrid(u,u,u)
#E field
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex,v=Ey,w=Ez)]
positive = [go.Scatter3d(x=xpos[q>0],y=ypos[q>0],z=zpos[q>0],mode='markers')]
negative = [go.Scatter3d(x=xpos[q<0],y=ypos[q<0],z=zpos[q<0],mode='markers')]
go.Figure(data=vector+positive+negative).show()