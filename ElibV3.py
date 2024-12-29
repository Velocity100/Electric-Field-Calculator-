#%%
import numpy as np

k = 1/(4*np.pi*8.85418781762039e-12)
#2d and 3d verions 
#from V3 to V2: no functions within functions
#avg=average, pos=position, coords=coordinates
#coords must be a meshgrid; pos must be arrays/lists
#if you have multiple charge distributions, just append all xpos, ypos, zpos, and Q's in one array 

def E3d(x_coords,y_coords,z_coords,Q,xpos,ypos,zpos): 
    #position vector, R
    position_vector = (np.dstack((xpos,ypos,zpos)))[0]
    if type(x_coords)==int:
        coordinate_vector = (np.dstack((x_coords,y_coords,z_coords)))[0] 
    else:
        #ravel the meshgrid
        coordinate_vector = (np.dstack((x_coords.ravel(),y_coords.ravel(),z_coords.ravel())))[0] 
    #Coulomb's Law
    Ex,Ey,Ez = 0,0,0
    for i in range(len(position_vector)):
        R = coordinate_vector-position_vector[i]
        R_mag = np.linalg.norm(R,axis=1)[:,np.newaxis]
        dE = (k*Q[i]*R)/(R_mag**3)
        Ex += dE[:,0]
        Ey += dE[:,1]
        Ez += dE[:,2]
    #|E|
    E = (np.dstack((Ex,Ey,Ez)))[0]
    E_mag = np.linalg.norm(E,axis=1)
    E_mag = E_mag[~np.isnan(E_mag)]

    return Ex,Ey,Ez,E_mag
    
#same as above but for 2D
def E2d(x_coords,y_coords,Q,xpos,ypos): 
    position_vector = (np.dstack((xpos,ypos)))[0]
    if type(x_coords)==int:
        coordinate_vector = (np.dstack((x_coords,y_coords)))[0] 
    else:
        coordinate_vector = (np.dstack((x_coords.ravel(),y_coords.ravel())))[0] 
    Ex,Ey = 0,0
    for i in range(len(position_vector)):
        R = coordinate_vector-position_vector[i]
        R_mag = np.linalg.norm(R,axis=1)[:,np.newaxis]
        dE = (k*Q[i]*R)/(R_mag**3)
        Ex += dE[:,0]
        Ey += dE[:,1]
    E = (np.dstack((Ex,Ey)))[0]
    E_mag = np.linalg.norm(E,axis=1)
    E_mag = E_mag[~np.isnan(E_mag)]
    #if using matplotlib stream plot, reshape Ex and Ey --> Ex = Ex.shape((x_coords.shape)) and same for Ey
    return Ex,Ey,E,E_mag


import plotly.graph_objects as go
rxy = 2
rz = 2
s1 = 0.25
x, y, z = np.meshgrid(np.arange(-rxy, rxy, s1),
                      np.arange(-rxy, rxy, s1),
                      np.arange(-rz, rz, s1))

zpos1 = z.ravel()*0.5
ypos1, xpos1  = y.ravel()*0.5, np.ones_like(zpos1)*0.5
q1 = np.ones_like(zpos1)

xpos2, ypos2, zpos2,q2 = np.ones_like(zpos1)*-0.5, y.ravel()*0.5,z.ravel()*0.5,np.ones_like(zpos1)*-1

xpos,ypos,zpos,q=np.append(xpos1,xpos2),np.append(ypos1,ypos2),np.append(zpos1,zpos2),np.append(q1,q2)
Ex,Ey,Ez = E3d(x,y,z,q,xpos,ypos,zpos)
go.Figure(go.Cone(x=x.ravel(),y=y.ravel(),z=z.ravel(),u=Ex,v=Ey,w=Ez)).show()
