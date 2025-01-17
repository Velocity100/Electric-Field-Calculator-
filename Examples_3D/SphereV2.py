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

    return x,y,z
#sphere positions and charges
r1=1
xpos,ypos,zpos = sph(r1,1e6*5)
q = np.ones_like(xpos)

#make grid
u = np.linspace(-4,4,20)
x,y,z = np.meshgrid(u,u,u)
#E field
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)[:3]
#plot 3d vector field
import plotly.graph_objects as go
vector = [go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex.ravel(),v=Ey.ravel(),w=Ez.ravel())]
positive = [go.Scatter3d(x=xpos,y=ypos,z=zpos,mode='markers',line=dict(color='blue'))]
fig=go.Figure(data=vector+positive).show()

#E magnitude plot along x axis
w = np.linspace(-r1,r1+5*r1,1000)
w1 = np.zeros(1000)
Emag = E3d(w,w1,w1,q,xpos,ypos,zpos)[3]
import plotly.express as px
px.line(x=w,y=Emag).show()

#E magnitude from code vs Coulomb's Law for a point charge
k = 1/(4*np.pi*8.85418781762039e-12)
r = 5000
Eexp = k*len(q)/r**2
Eth = E3d(r,0,0,q,xpos,ypos,zpos)[3]
print(f"{(Eexp-Eth)/Eexp*100:.5%} error")

