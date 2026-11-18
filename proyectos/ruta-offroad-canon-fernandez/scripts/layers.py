# Build co-registered 10 m... use 20 m grid in UTM13N over study area
import rasterio, numpy as np
from rasterio.warp import reproject, Resampling
from rasterio.transform import from_origin
D='../dl/'
x0,x1,y0,y1=610000,665000,2795000,2850000
res=20
W=int((x1-x0)/res);H=int((y1-y0)/res)
tr=from_origin(x0,y1,res,res)
def rp(f,band=1,rs=Resampling.bilinear,dtype='float32'):
    out=np.zeros((H,W),dtype)
    with rasterio.open(f) as r:
        reproject(rasterio.band(r,band),out,dst_transform=tr,dst_crs='EPSG:32613',resampling=rs)
    return out
dem=rp(D+'dem_N25W104.tif')
red=rp(D+'s2_B04.tif').astype('float32');nir=rp(D+'s2_B08.tif').astype('float32')
ndvi=(nir-red)/(nir+red+1e-6)
rgb=np.stack([rp(D+'s2_TCI.tif',b,dtype='uint8') for b in (1,2,3)],-1)
gy,gx=np.gradient(dem,res)
slope=np.degrees(np.arctan(np.hypot(gx,gy)))
np.savez_compressed('layers.npz',dem=dem,ndvi=ndvi,slope=slope,rgb=rgb,x0=x0,y1=y1,res=res)
print(dem.min(),dem.max(),np.percentile(ndvi,[5,50,95,99]),np.percentile(slope,[50,90,99]))
