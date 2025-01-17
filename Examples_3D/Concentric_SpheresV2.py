import numpy as np
from ElibV3 import E3d

#make sphere from fibonacci sequence
def sph(r=1,samples=1000):
    x,y,z=[],[],[]
    phi = np.pi * (np.sqrt(5.) - 1.)  # golden angle in radians
    samples = int(samples)
    for i in range(samples):
        y_sph = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y_sph * y_sph)  # radius at y
        theta = phi * i  # golden angle increment
        x_sph = np.cos(theta) * radius
        z_sph = np.sin(theta) * radius

        x_sph,y_sph,z_sph = x_sph*r,y_sph*r,z_sph*r
        x.append(x_sph)
        y.append(y_sph)
        z.append(z_sph)
    x,y,z = np.array([x,y,z])
    return x,y,z

#sphere 1 and 2 positions and charges
r1 = 1
r2 = r1/2
n = 1e3 #multiples of 10 seem to work best for magnitude plot
x_r1,y_r1,z_r1 = sph(r1,n)
x_r2,y_r2,z_r2 = sph(r2,n)
xpos,ypos,zpos = np.append(x_r1,x_r2),np.append(y_r1,y_r2),np.append(z_r1,z_r2)
q_r1 = np.ones_like(x_r1)
q_r2 = -np.ones_like(x_r2)
q = np.append(q_r1,q_r2)

#make grid
u = np.linspace(-1.5,1.5,20)
x,y,z = np.meshgrid(u,u,u)
#E field
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex.ravel(),v=Ey.ravel(),w=Ez.ravel())]
positive = [go.Scatter3d(x=xpos[q>0],y=ypos[q>0],z=zpos[q>0],mode='markers',line=dict(color='blue'))]
negative = [go.Scatter3d(x=xpos[q<0],y=ypos[q<0],z=zpos[q<0],mode='markers',line=dict(color='red'))]
fig=go.Figure(data=positive+negative)
fig.show()
#plot magnitude of total E field along x axis from -r1 to 2*r1
w = np.linspace(-r1,r1+1*r1,1000)
w1 = np.zeros(1000)
Emag = E3d(w,w1,w1,q,xpos,ypos,zpos)[3]
import plotly.express as px
px.line(x=w,y=Emag).show()