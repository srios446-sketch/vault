import numpy as np, json
from skimage.graph import route_through_array
from scipy import ndimage as ndi
from pyproj import Transformer
L=np.load('layers.npz'); x0,y1,res=int(L['x0']),int(L['y1']),int(L['res'])
dem,sl,nd=L['dem'],L['slope'],L['ndvi']
steep=ndi.binary_dilation(sl>20,iterations=10)  # 200 m alrededor de laderas >20°
cost=np.where(sl<3,1.0,np.where(sl<12,0.8,np.where(sl<18,2.5,8.0)))
cost[nd>0.40]=40         # cultivos / vegetación riparia
cost[steep]=60
import sys; k=float(sys.argv[1]) if len(sys.argv)>1 else 1.0; C=(627800,2830000)
W0=[(628000,2826500),(625000,2827800),(624000,2830500),(624900,2832600),(627400,2832700),(628300,2830000)]
WP=[W0[0]]+[(int(C[0]+k*(x-C[0])),int(C[1]+k*(y-C[1]))) for x,y in W0[1:]]+[W0[0]]
rc=lambda x,y:(int((y1-y)/res),int((x-x0)/res))
path=[];c=cost.copy()
for a,b in zip(WP[:-1],WP[1:]):
    p,_=route_through_array(c,rc(*a),rc(*b),fully_connected=True,geometric=True)
    path+=p if not path else p[1:]
    for r,cc in p: c[max(r-2,0):r+3,max(cc-2,0):cc+3]*=3   # no repetir tramo
P=np.array(path); xs=x0+(P[:,1]+.5)*res; ys=y1-(P[:,0]+.5)*res
d=np.r_[0,np.cumsum(np.hypot(np.diff(xs),np.diff(ys)))]
z=dem[P[:,0],P[:,1]]; s=sl[P[:,0],P[:,1]]; n=nd[P[:,0],P[:,1]]
print('km',d[-1]/1000,'z',z.min(),z.max(),'gain',np.clip(np.diff(ndi.uniform_filter1d(z,15)),0,None).sum())
print('slope pct>12',(s>12).mean(),'ndvi>0.4',(n>0.4).mean(),'steep',steep[P[:,0],P[:,1]].mean())
np.savez('route.npz',xs=xs,ys=ys,d=d,z=z,s=s,n=n,WP=np.array(WP))
