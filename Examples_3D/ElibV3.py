
import numpy as np

k = 1/(4*np.pi*8.85418781762039e-12)
#2d and 3d verions 
#from V3 to V2: no functions within functions
#avg=average, pos=position, coords=coordinates
#coords and positions must be lists/arrays
#if you have multiple charge distributions, must append all xpos, ypos, zpos, and Q's in one list/array 

def E3d(x_coords,y_coords,z_coords,Q,xpos,ypos,zpos): 
    #position vector, R
    position_vector = (np.dstack((xpos,ypos,zpos)))[0]
    if type(x_coords)==(int or float):
        coordinate_vector = (np.dstack((x_coords,y_coords,z_coords)))[0] 
    elif type(x_coords)==list:
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
    #E field magnitude
    E = (np.dstack((Ex,Ey,Ez)))[0]
    E_mag = np.linalg.norm(E,axis=1)
    E_mag = E_mag[~np.isnan(E_mag)]

    return Ex,Ey,Ez,E_mag if len(E_mag)>1 else E_mag[0]
    
#same as above but for 2D
def E2d(x_coords,y_coords,Q,xpos,ypos): 
    position_vector = (np.dstack((xpos,ypos)))[0]
    if type(x_coords)==(int or float):
        coordinate_vector = (np.dstack((x_coords,y_coords)))[0] 
    elif type(x_coords)==list:
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


