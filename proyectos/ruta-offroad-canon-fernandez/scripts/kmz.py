# KMZ: ruta + estaciones + kilometraje + imagen Sentinel-2 (GroundOverlay)
# Uso: python3 kmz.py <carpeta_con_s2_TCI.tif>
import sys, json, zipfile, numpy as np, rasterio
from rasterio.warp import reproject, Resampling
from rasterio.transform import from_bounds
from PIL import Image

DL = sys.argv[1]
OUT = '/home/user/vault/proyectos/ruta-offroad-canon-fernandez/datos/'
W, S, E, N = -103.79, 25.53, -103.70, 25.625
w = 1400; h = int(w * (N - S) / (E - W) * 1.1)
tr = from_bounds(W, S, E, N, w, h)
rgb = np.zeros((3, h, w), 'uint8')
with rasterio.open(DL + '/s2_TCI.tif') as r:
    for b in range(3):
        reproject(rasterio.band(r, b + 1), rgb[b], dst_transform=tr, dst_crs='EPSG:4326', resampling=Resampling.bilinear)
jpg = DL + '/s2_overlay.jpg'
Image.fromarray(np.clip(rgb.transpose(1, 2, 0) * 1.7, 0, 255).astype('uint8')).save(jpg, quality=88)

g = json.load(open(OUT + 'ruta.geojson'))
line = g['features'][0]['geometry']['coordinates']
pts = g['features'][1:]
k = ['<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document>',
     '<name>Circuito El Lomerío (preliminar, 20.2 km)</name>',
     '<Style id="r"><LineStyle><color>ff303bff</color><width>5</width></LineStyle></Style>',
     '<Style id="e"><IconStyle><color>ff59c734</color><scale>1.2</scale></IconStyle></Style>',
     '<Style id="k"><IconStyle><scale>0.5</scale></IconStyle><LabelStyle><scale>0.7</scale></LabelStyle></Style>',
     f'<Folder><name>Imagen Sentinel-2 (14-nov-2026)</name><GroundOverlay><name>Sentinel-2 color natural</name>'
     f'<Icon><href>s2.jpg</href></Icon><LatLonBox><north>{N}</north><south>{S}</south><east>{E}</east><west>{W}</west></LatLonBox></GroundOverlay></Folder>',
     '<Placemark><name>Ruta 20.2 km</name><description>Propuesta preliminar. No transitar sin autorización ejidal '
     'ni sin verificar el polígono del ANP federal.</description><styleUrl>#r</styleUrl><LineString><tessellate>1</tessellate><coordinates>'
     + ' '.join(f'{c[0]},{c[1]},{c[2]}' for c in line[::2]) + '</coordinates></LineString></Placemark>',
     '<Folder><name>Estaciones</name>']
k += [f'<Placemark><name>{p["properties"]["id"]} · {p["properties"]["nombre"]}</name><description>Km {p["properties"]["km"]}</description>'
      f'<styleUrl>#e</styleUrl><Point><coordinates>{p["geometry"]["coordinates"][0]},{p["geometry"]["coordinates"][1]}</coordinates></Point></Placemark>' for p in pts]
k += ['</Folder><Folder><name>Kilometraje</name>']
d = np.r_[0, np.cumsum([np.hypot((a[0] - b[0]) * 100.4e3, (a[1] - b[1]) * 110.9e3) for a, b in zip(line[:-1], line[1:])])]
for km in range(1, 21):
    i = int(np.argmin(abs(d - km * 1000)))
    k.append(f'<Placemark><name>km {km}</name><styleUrl>#k</styleUrl><Point><coordinates>{line[i][0]},{line[i][1]}</coordinates></Point></Placemark>')
k += ['</Folder></Document></kml>']
with zipfile.ZipFile(OUT + 'ruta.kmz', 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('doc.kml', ''.join(k))
    z.write(jpg, 's2.jpg')
print('ok', round(d[-1] / 1000, 2), 'km')
