import numpy as np, json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter1d as u
from pyproj import Transformer
L=np.load('layers.npz'); R=np.load('route.npz'); x0,y1,res=int(L['x0']),int(L['y1']),int(L['res'])
xs,ys=u(R['xs'],9,mode='wrap'),u(R['ys'],9,mode='wrap'); xs[-1],ys[-1]=xs[0],ys[0]
d=np.r_[0,np.cumsum(np.hypot(np.diff(xs),np.diff(ys)))]; z=u(R['z'],7,mode='nearest'); n=R['n']
inv=Transformer.from_crs(32613,4326,always_xy=True); fw=Transformer.from_crs(4326,32613,always_xy=True)
lon,lat=inv.transform(xs,ys)
# grade
k=25; gr=np.zeros_like(z); gr[k:-k]=(z[2*k:]-z[:-2*k])/(d[2*k:]-d[:-2*k])*100
print('len',d[-1],'zmin',z.min(),'zmax',z.max(),'up',np.clip(np.diff(z),0,None).sum(),'grade p95',np.percentile(abs(gr),95),'max',abs(gr).max())
def at(km): i=np.argmin(abs(d-km*1000)); return i
# riparian crossings
rip=np.where(n>0.33)[0]; print('rip idx',rip[:50], d[rip][:50] if len(rip) else '')
ramsar=fw.transform(-103.726,25.340); print('dist ramsar km', np.min(np.hypot(xs-ramsar[0],ys-ramsar[1]))/1000)
for nm,(la,lo) in {'Sapioris':(25.4524,-103.7168),'JuanEGarcia':(25.4918,-103.6908),'LeonGuzman':(25.5013,-103.6591)}.items():
    X,Y=fw.transform(lo,la); print(nm, np.min(np.hypot(xs-X,ys-Y))/1000)
ihi=np.argmax(z); print('high',d[ihi],lat[ihi],lon[ihi])
np.savez('final.npz',xs=xs,ys=ys,d=d,z=z,gr=gr,lat=lat,lon=lon,n=n)
