import numpy as np
from ElibV3 import E3d

#make grid; this time used for both coordinates and positions 
u = np.arange(-4,4,0.25)
x, y, z = np.meshgrid(u,u,u)

zpos1 = z.ravel()*0.5
ypos1, xpos1  = y.ravel()*0.5, np.ones_like(zpos1)*0.5
q1 = np.ones_like(zpos1)

xpos2, ypos2, zpos2, q2 = np.ones_like(zpos1)*-0.5, y.ravel()*0.5,z.ravel()*0.5,np.ones_like(zpos1)*-1

xpos,ypos,zpos,q=np.append(xpos1,xpos2),np.append(ypos1,ypos2),np.append(zpos1,zpos2),np.append(q1,q2)
#E field
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex,v=Ey,w=Ez)]
positive = [go.Scatter3d(x=xpos[q>0],y=ypos[q>0],z=zpos[q>0],mode='markers')]
negative = [go.Scatter3d(x=xpos[q<0],y=ypos[q<0],z=zpos[q<0],mode='markers')]
go.Figure(data=vector+positive+negative).show()