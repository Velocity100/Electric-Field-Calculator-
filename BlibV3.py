#%%
import numpy as np

#from V3 to V2: no functions within functions
#avg=average, pos=position, coords=coordinates
#coords must be a meshgrid; pos must be arrays/lists
def B(x_coords,y_coords,z_coords,x_position_of_wire,y_position_of_wire,z_position_of_wire,I=1): 
    #mu_o*I/(4*pi)                     
    C = I*10**-7
    #one wire or multiple:
        #1 wire
    if len(x_position_of_wire.shape)==1: 
        #vertical stacking for quick calculation
        L = np.vstack((x_position_of_wire,y_position_of_wire,z_position_of_wire))
        #dl vector
        dlx,dly,dlz = L[:,1:]-L[:,:-1]
        #dl vector position
        dlx_avg_pos,dly_avg_pos,dlz_avg_pos = ((L[:,1:]+L[:,:-1])*0.5)
    #multiple wires, i.e. helmholtz. MUST define each x, y z position then vstack each. For ex, for x positions: (np.vstack(x1,x2,x3)); 
    else: 
        L = np.vstack(([x_position_of_wire],[y_position_of_wire],[z_position_of_wire]))
        dlx,dly,dlz = (L[:,:,1:]-L[:,:,:-1]).reshape(((3,(L.shape[1])*(L.shape[2]-1))))
        dlx_avg_pos,dly_avg_pos,dlz_avg_pos = ((L[:,:,1:]+L[:,:,:-1])*0.5).reshape(((3,(L.shape[1])*(L.shape[2]-1))))   
    #Biot-Savart Law     
    Bx,By,Bz=0,0,0
    for i in range(len(dlx)): 
        Rx,Ry,Rz = x_coords-dlx_avg_pos[i], y_coords-dly_avg_pos[i], z_coords-dlz_avg_pos[i]
        R = np.sqrt(((Rx)**2 + (Ry)**2 + (Rz)**2))
        crossx,crossy,crossz = dly[i]*Rz - dlz[i]*Ry, dlz[i]*Rx - dlx[i]*Rz, dlx[i]*Ry - dly[i]*Rx
        dBx,dBy,dBz = C*crossx/(R**3),C*crossy/(R**3),C*crossz/(R**3)
        Bx+=dBx
        By+=dBy
        Bz+=dBz
    #|B|
    B = (np.dstack((Bx,By,Bz)))[0] 
    B_mag = np.linalg.norm(B,axis=1)
    return Bx,By,Bz,B,B_mag

