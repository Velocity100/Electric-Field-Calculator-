import numpy as np
from ElibV3 import E3d
#parameterization
angles = np.arange(0,2*np.pi,np.pi/6)
qs = np.arange(0,12*np.pi,np.pi)
#positions 
xpos = np.cos(angles)
ypos = np.sin(angles)
zpos =np.zeros_like(xpos)
#charge
q = np.cos(qs)
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