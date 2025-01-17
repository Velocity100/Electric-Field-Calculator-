import numpy as np
from ElibV3 import E3d
#positions and charges
xpos,ypos,zpos,q = [-1,1],[0,0],[0,0],[-1,1]
#make grid 
u = np.linspace(-1.5,1.5,10)
x,y,z = np.meshgrid(u,u,u)
#E field
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex,v=Ey,w=Ez)]
positive = [go.Scatter3d(x=[1],y=[0],z=[0],mode='markers')]
negative = [go.Scatter3d(x=[-1],y=[0],z=[0],mode='markers')]
go.Figure(data=vector+positive+negative).show()