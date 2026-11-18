# Ruta off-road fuera del Cañón de Fernández

Proyecto personal de Sebastian y su novia. Iniciado el 2026-11-18.

## Objetivo
Una ruta para motos y vehículos todo terreno que sea divertida y tenga buenas vistas y paraderos. Tiene que quedar FUERA de las áreas protegidas del Cañón de Fernández (Lerdo, Dgo.), donde el tránsito off-road daña la flora y la fauna. Además debe dejar derrama económica en los ejidos cercanos con renta de espacios, comida, cuotas y guías.

## Entregables
| # | Entregable | Estado |
|---|---|---|
| 1 | PDF con una ruta de 20 km: `ruta-20km-preliminar.pdf` | Hecho, preliminar (2026-11-18) |

## Ruta v1: Circuito "El Lomerío"
- Circuito de 20.2 km. Sale en 25.55015, -103.72577, al norte de Juan E. García.
- Altitud de 1,193 a 1,267 m. Desnivel acumulado de unos 100 m. Pendiente menor a 3%.
- Queda a unos 22.5 km del centro del sitio Ramsar 1747.
- Archivos en `datos/`: ruta.kmz (Google Earth, con kilometraje e imagen satelital), ruta.gpx, ruta.kml, ruta.geojson y los mapas.
- Scripts en `scripts/`: layers → route → outputs → figs → pdf. Los insumos se descargan de AWS Open Data: Copernicus DEM y Sentinel-2 L2A, escena 13RFJ del 2026-11-14.

## Hallazgos clave
- Desde el DOF del 08-01-2024 el cañón quedó dentro del ANP federal **"Ríos y Montañas de la Comarca Lagunera"**: unas 172,924 ha que administra CONANP. La ruta debe quedar fuera de ese polígono, que **todavía no tenemos** porque la red de la sesión bloquea dof.gob.mx y simec.conanp.gob.mx.
- Santa Anita (225 hab.) y Santo Niño no están georreferenciados con fuentes confiables. Una fuente pone Santa Anita a unos 27 km al NO de Cd. Lerdo, así que podría estar cerca del circuito. Falta verificarlo.
- En 2026 ya hubo operativos contra razers en el cañón, entrando por Sapioriz.

## Agentes del proyecto (`.claude/agents/`)
- ruta-ambiental: normativa, ANP, especies.
- ruta-economia: ejidos, mercado, derrama.
- ruta-geoespacial: imágenes satelitales, DEM y trazo.

## Siguientes pasos
1. Conseguir el polígono oficial del ANP federal y sobreponerlo al trazo.
2. Ubicar en campo Santa Anita y Santo Niño.
3. Recorrido de reconocimiento con el GPX.
4. Identificar el ejido dueño del terreno (RAN) y presentar el proyecto en asamblea.
5. Consulta previa con SRNyMA Durango y CONANP.
