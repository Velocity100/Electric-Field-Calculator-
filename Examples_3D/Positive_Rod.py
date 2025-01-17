import numpy as np
from ElibV3 import E3d
#positions and charges
xpos,ypos,zpos,q = np.linspace(-5,5,1000),np.zeros(1000),np.zeros(1000),np.ones(1000)
#make grid
u = np.linspace(-5,5,20)
x,y,z = np.meshgrid(u,u,u)
#E field
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex,v=Ey,w=Ez)]
positive = [go.Scatter3d(x=xpos[q>0],y=ypos[q>0],z=zpos[q>0],mode='markers')]
negative = [go.Scatter3d(x=xpos[q<0],y=ypos[q<0],z=zpos[q<0],mode='markers')]
go.Figure(data=vector+positive+negative).show()