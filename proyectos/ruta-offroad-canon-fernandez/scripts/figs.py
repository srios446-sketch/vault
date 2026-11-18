import numpy as np, json, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pyproj import Transformer
OUT='/home/user/vault/proyectos/ruta-offroad-canon-fernandez/'
L=np.load('layers.npz'); F=np.load('final.npz'); x0,y1,res=int(L['x0']),int(L['y1']),int(L['res'])
xs,ys,d,z,lat,lon,n=[F[k] for k in ('xs','ys','d','z','lat','lon','n')]
fw=Transformer.from_crs(4326,32613,always_xy=True); inv=Transformer.from_crs(32613,4326,always_xy=True)
def crop(X0,X1,Y0,Y1,g=1.7):
    c0,c1=(X0-x0)//res,(X1-x0)//res; r0,r1=(y1-Y1)//res,(y1-Y0)//res
    return np.clip(L['rgb'][r0:r1,c0:c1].astype(float)*g,0,255).astype('uint8'),(r0,r1,c0,c1)
def lonlat_ticks(ax,X0,X1,Y0,Y1,step):
    xt=np.arange(X0,X1+1,step); yt=np.arange(Y0,Y1+1,step)
    ax.set_xticks(xt); ax.set_xticklabels([f'{inv.transform(x,(Y0+Y1)/2)[0]:.3f}' for x in xt],fontsize=7)
    ax.set_yticks(yt); ax.set_yticklabels([f'{inv.transform((X0+X1)/2,y)[1]:.3f}' for y in yt],fontsize=7)
    ax.grid(color='w',lw=.3,alpha=.5)
ST=[(0,'E1','Base / caseta ejidal\ny estacionamiento'),(5.0,'E2','Paradero poniente\n(sombra y agua)'),(9.2,'E3','Mirador norte\n(punto más alto)'),(14.5,'E4','Paradero oriente\n(comida local)')]
idx=lambda km:int(np.argmin(abs(d-km*1000)))
# 1 ubicación
X0,X1,Y0,Y1=612000,662000,2797000,2845000
img,_=crop(X0,X1,Y0,Y1)
fig,ax=plt.subplots(figsize=(8,7.7)); ax.imshow(img,extent=[X0,X1,Y0,Y1])
ax.plot(xs,ys,color='#ff3b30',lw=2.2,label='Ruta propuesta (20.2 km)')
rx,ry=fw.transform(-103.726,25.340)
ax.add_patch(Circle((rx,ry),6000,fill=True,fc=(1,0.85,0,.18),ec='#ffcc00',lw=1.5,ls='--'))
ax.plot(rx,ry,'*',color='#ffcc00',ms=14,mec='k',label='Cañón de Fernández (centro sitio Ramsar 1747)')
ax.text(rx+700,ry-1800,'Cañón de Fernández\n(zona aproximada, NO es\nel polígono oficial)',color='#ffcc00',fontsize=8,weight='bold')
for nm,(la,lo) in {'Sapioris':(25.4524,-103.7168),'Juan E. García':(25.4918,-103.6908),'León Guzmán':(25.5013,-103.6591),'Cd. Juárez':(25.4944,-103.5958)}.items():
    X,Y=fw.transform(lo,la); ax.plot(X,Y,'o',color='#5ac8fa',mec='k',ms=6); ax.text(X+500,Y+300,nm,color='w',fontsize=8,weight='bold')
ax.annotate('',xy=(xs[0],ys[0]-300),xytext=(rx,ry+6200),arrowprops=dict(arrowstyle='<->',color='w',lw=1))
ax.text(rx-9500,(ys[0]+ry)/2+3000,'≈ 22.5 km al centro\ndel sitio Ramsar',color='w',fontsize=8,weight='bold',bbox=dict(fc=(0,0,0,.5),ec='none'))
lonlat_ticks(ax,X0,X1,Y0,Y1,10000); ax.set_xlabel('Longitud',fontsize=8); ax.set_ylabel('Latitud',fontsize=8)
ax.legend(loc='upper right',fontsize=7,framealpha=.85)
ax.set_title('Ubicación de la ruta respecto al Cañón de Fernández',fontsize=10)
plt.savefig(OUT+'datos/mapa_ubicacion.png',dpi=170,bbox_inches='tight'); plt.close()
# 2 detalle
X0,X1,Y0,Y1=621500,631000,2824500,2835000
img,(r0,r1,c0,c1)=crop(X0,X1,Y0,Y1,1.8)
fig,ax=plt.subplots(figsize=(8,8.6)); ax.imshow(img,extent=[X0,X1,Y0,Y1])
ax.contour(np.linspace(X0,X1,c1-c0),np.linspace(Y1,Y0,r1-r0),L['dem'][r0:r1,c0:c1],levels=range(1180,1700,20),colors='k',linewidths=.25,alpha=.6)
ax.plot(xs,ys,color='k',lw=4.5); ax.plot(xs,ys,color='#ff3b30',lw=2.6)
for km in range(1,20):
    i=idx(km); ax.text(xs[i],ys[i],str(km),fontsize=6.5,ha='center',va='center',color='k',bbox=dict(boxstyle='circle,pad=0.15',fc='w',ec='k',lw=.4))
for km,c,t in ST:
    i=idx(km); ax.plot(xs[i],ys[i],'s',ms=11,color='#34c759',mec='k'); ax.text(xs[i]+250,ys[i]+150,f'{c} · {t}',fontsize=7.5,color='w',weight='bold',bbox=dict(fc=(0,0,0,.55),ec='none',pad=2))
ax.plot([X1-2200,X1-1200],[Y0+400]*2,'k-',lw=3); ax.text(X1-1700,Y0+550,'1 km',color='k',ha='center',fontsize=8,weight='bold')
lonlat_ticks(ax,X0,X1,Y0,Y1,2000)
ax.set_title('Circuito "El Lomerío": trazo, kilometraje y estaciones (curvas cada 20 m)',fontsize=10)
plt.savefig(OUT+'datos/mapa_detalle.png',dpi=170,bbox_inches='tight'); plt.close()
# 3 perfil
fig,(a1,a2)=plt.subplots(2,1,figsize=(8,3.6),sharex=True,gridspec_kw={'height_ratios':[3,1.3]})
a1.fill_between(d/1000,z,z.min()-15,color='#c69c6d',alpha=.6); a1.plot(d/1000,z,color='#7a4e1d',lw=1.4)
for km,c,t in ST: i=idx(km); a1.plot(d[i]/1000,z[i],'s',color='#34c759',mec='k'); a1.text(d[i]/1000,z[i]+6,c,fontsize=8,ha='center')
a1.set_ylabel('Altitud (m)',fontsize=8); a1.set_ylim(z.min()-15,z.max()+25); a1.grid(alpha=.3); a1.tick_params(labelsize=7)
a1.set_title('Perfil de elevación y vegetación a lo largo de la ruta',fontsize=10)
a2.fill_between(d/1000,n,0,color='#4cd964',alpha=.7); a2.axhline(0.5,color='r',lw=.7,ls='--'); a2.set_ylabel('NDVI',fontsize=8); a2.set_xlabel('Kilómetro',fontsize=8); a2.tick_params(labelsize=7); a2.grid(alpha=.3); a2.set_ylim(0,max(.7,n.max()))
plt.savefig(OUT+'datos/perfil.png',dpi=170,bbox_inches='tight'); plt.close()
# vectores
co=list(zip(np.round(lon,6),np.round(lat,6),np.round(z,1)))
stp=[{'type':'Feature','geometry':{'type':'Point','coordinates':[round(float(lon[idx(k)]),6),round(float(lat[idx(k)]),6)]},'properties':{'id':c,'km':k,'nombre':t.replace('\n',' ')}} for k,c,t in ST]
gj={'type':'FeatureCollection','features':[{'type':'Feature','geometry':{'type':'LineString','coordinates':[list(map(float,c)) for c in co]},'properties':{'nombre':'Circuito El Lomerío (preliminar)','km':round(float(d[-1]/1000),2)}}]+stp}
json.dump(gj,open(OUT+'datos/ruta.geojson','w'))
g=['<?xml version="1.0" encoding="UTF-8"?>','<gpx version="1.1" creator="vault" xmlns="http://www.topografix.com/GPX/1/1">']
g+=[f'<wpt lat="{f["geometry"]["coordinates"][1]}" lon="{f["geometry"]["coordinates"][0]}"><name>{f["properties"]["id"]} {f["properties"]["nombre"]}</name></wpt>' for f in stp]
g+=['<trk><name>Circuito El Lomerio (preliminar)</name><trkseg>']+[f'<trkpt lat="{b}" lon="{a}"><ele>{c}</ele></trkpt>' for a,b,c in co[::2]]+['</trkseg></trk></gpx>']
open(OUT+'datos/ruta.gpx','w').write('\n'.join(g))
k=['<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Circuito El Lomerío</name><Style id="r"><LineStyle><color>ff303bff</color><width>4</width></LineStyle></Style>']
k+=[f'<Placemark><name>{f["properties"]["id"]} {f["properties"]["nombre"]}</name><Point><coordinates>{f["geometry"]["coordinates"][0]},{f["geometry"]["coordinates"][1]}</coordinates></Point></Placemark>' for f in stp]
k+=['<Placemark><name>Ruta 20.2 km</name><styleUrl>#r</styleUrl><LineString><coordinates>'+' '.join(f'{a},{b}' for a,b,c in co[::2])+'</coordinates></LineString></Placemark></Document></kml>']
open(OUT+'datos/ruta.kml','w').write(''.join(k))
json.dump({'st':[(k,c,t.replace('\n',' '),float(lat[idx(k)]),float(lon[idx(k)]),float(z[idx(k)])) for k,c,t in ST],'len':float(d[-1]),'zmin':float(z.min()),'zmax':float(z.max()),'up':float(np.clip(np.diff(z),0,None).sum()),'ndvi50':float((n>0.5).mean()),'ndvimed':float(np.median(n))},open('summary.json','w'))
print(open('summary.json').read())
