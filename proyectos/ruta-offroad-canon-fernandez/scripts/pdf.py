import json
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
OUT='/home/user/vault/proyectos/ruta-offroad-canon-fernandez/'
S=json.load(open('summary.json'))
ss=getSampleStyleSheet()
H1=ParagraphStyle('h1',parent=ss['Heading1'],fontSize=17,textColor=colors.HexColor('#7a3d0a'),spaceAfter=6)
H2=ParagraphStyle('h2',parent=ss['Heading2'],fontSize=12.5,textColor=colors.HexColor('#7a3d0a'),spaceBefore=8,spaceAfter=4)
B=ParagraphStyle('b',parent=ss['BodyText'],fontSize=9.3,leading=12.5)
SM=ParagraphStyle('sm',parent=B,fontSize=7.6,leading=9.6,textColor=colors.HexColor('#444444'))
AL=ParagraphStyle('al',parent=B,backColor=colors.HexColor('#fff4d6'),borderColor=colors.HexColor('#e0a800'),borderWidth=.8,borderPadding=6,spaceBefore=6,spaceAfter=10)
P=lambda t,s=B:Paragraph(t,s)
def tbl(rows,w,head=True):
    t=Table([[P(c,SM if len(rows)>8 else B) if isinstance(c,str) else c for c in r] for r in rows],colWidths=w)
    st=[('GRID',(0,0),(-1,-1),.4,colors.HexColor('#bbbbbb')),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),3),('TOPPADDING',(0,0),(-1,-1),3)]
    if head: st+=[('BACKGROUND',(0,0),(-1,0),colors.HexColor('#f1e4d3'))]
    t.setStyle(TableStyle(st)); return t
st=S['st']
E=[]
E+=[P('Circuito off-road "El Lomerío"',H1),
P('<b>Propuesta preliminar de ruta de 20 km para motos y vehículos todo terreno, fuera del Cañón de Fernández</b><br/>Lerdo, Durango · Primer entregable · 18 de noviembre de 2026 · Sebastian y su pareja (proyecto personal)',B),Spacer(1,6),
P('<b>Estado: PRELIMINAR (análisis de escritorio).</b> El trazo se hizo con imagen satelital y modelo de elevación. Todavía falta confirmar tres cosas: (1) el polígono oficial del ANP federal "Ríos y Montañas de la Comarca Lagunera" (2024), (2) qué ejido es dueño del terreno y (3) cómo están las brechas en campo. Mientras eso no se confirme, no se debe abrir ni promover la ruta.',AL),
P('Ficha técnica',H2),
tbl([['Concepto','Valor'],
['Tipo de ruta','Circuito cerrado (sale y llega al mismo punto), sentido horario'],
['Longitud',f"{S['len']/1000:.1f} km"],
['Altitud mínima / máxima',f"{S['zmin']:.0f} m / {S['zmax']:.0f} m s.n.m."],
['Desnivel acumulado (subida)',f"aprox. {S['up']:.0f} m"],
['Pendiente del trazo','Menor a 3% en todo el recorrido (calculada con DEM de 30 m; en campo habrá desniveles cortos que el modelo no detecta)'],
['Dificultad','Baja-media. Ruta escénica de piedemonte y arroyo seco, para familias, motos de enduro y UTV/RZR. Las secciones técnicas son opcionales (ver sección 6)'],
['Punto de salida (E1)',f"{st[0][3]:.5f}, {st[0][4]:.5f}"],
['Distancia al centro del sitio Ramsar del Cañón de Fernández','aprox. 22.5 km al norte'],
['Localidades más cercanas','Juan E. García (aprox. 6.9 km), León Guzmán (aprox. 8.3 km), Sapioris (aprox. 10.2 km)'],
['Vegetación densa sobre el trazo (NDVI &gt; 0.5)',f"{S['ndvi50']*100:.1f}% del recorrido (NDVI mediano {S['ndvimed']:.2f}: matorral abierto y suelo desnudo)"],
],[5.2*cm,11.8*cm]),
Spacer(1,8),Image(OUT+'datos/mapa_ubicacion.png',width=10.6*cm,height=10.2*cm),
P('Imagen Sentinel-2 L2A del 14-nov-2026 (color natural). El círculo amarillo es una zona aproximada de 6 km alrededor del centro del sitio Ramsar 1747. NO es el polígono legal.',SM),
PageBreak(),
P('1. Trazo y estaciones',H2),
Image(OUT+'datos/mapa_detalle.png',width=15.2*cm,height=16.4*cm),Spacer(1,4),
tbl([['Est.','Km','Uso propuesto','Lat, Lon','Altitud']]+[[s[1],f"{s[0]:.1f}",s[2],f"{s[3]:.5f}, {s[4]:.5f}",f"{s[5]:.0f} m"] for s in st],[1.3*cm,1.2*cm,6.5*cm,5*cm,2*cm]),
PageBreak(),
Image(OUT+'datos/perfil.png',width=17*cm,height=7.6*cm),
P('2. Cómo se trazó (criterios)',H2),
P('La ruta sale de un análisis de <b>costo mínimo</b> sobre una malla de 20 m que combina tres capas: la topografía Copernicus DEM GLO-30, la imagen Sentinel-2 L2A (bandas rojo e infrarrojo para el índice de vegetación NDVI) y las pendientes derivadas del DEM. Las reglas fueron:'),
tbl([['Criterio','Regla aplicada','Motivo'],
['Áreas protegidas','Excluir toda la zona del cañón y el río Nazas aguas arriba de Sapioris. La ruta queda a más de 20 km del centro del ANP estatal','Objetivo central: no transitar por el cañón'],
['Sierras y laderas','Prohibido pasar por laderas de más de 20° ni a menos de 200 m de ellas','Evitar erosión y hábitat de rapaces, y porque el ANP federal incluye "montañas"'],
['Pendiente del trazo','Se prefieren terrenos de 3 a 12° y se penaliza por encima de 18°','Recomendación OHV: 10% en promedio y 15% como máximo en tramos cortos'],
['Vegetación','Penalizar NDVI &gt; 0.40 (cultivos, mezquital denso, vegetación de arroyo)','No dañar flora ni cultivos ejidales'],
['Sin tramos repetidos','Penalizar volver a pasar por celdas ya usadas','Que el circuito sea un anillo y no una ida y vuelta'],
['Comercio','Salida junto a la zona agrícola de Juan E. García / León Guzmán','Que la derrama quede en esas comunidades'],
],[3.3*cm,8*cm,5.7*cm]),
P('<b>Puntos a vigilar en campo:</b> entre los km 13.5 y 16.5 la ruta corre paralela a un arroyo con vegetación riparia, al oriente de la loma. Ahí conviene dejar al menos 100 m de separación y cruzar el arroyo en un solo punto, señalizado. Entre los km 0 y 2 y entre los km 17 y 20 la ruta bordea parcelas: hay que usar brechas ejidales que ya existan.',B),
PageBreak(),
P('3. Hallazgo crítico: el ANP ahora es federal y más grande',H2),
P('El Parque Estatal Cañón de Fernández (decreto del 25-abr-2004, aprox. 17,000 ha, sitio Ramsar 1747) quedó dentro del <b>Área de Protección de Recursos Naturales "Ríos y Montañas de la Comarca Lagunera"</b>. Su decreto se publicó en el DOF el 08-ene-2024 y cubre aprox. 172,924 ha en Lerdo, Nazas, Mapimí, Cuencamé y Gómez Palacio, incluidas las sierras El Sarnoso y La India. Hoy la administra CONANP. En 2026 hubo operativos que frenaron a unos 80 vehículos en el acceso por Sapioriz, y el nuevo Programa de Manejo va a restringir los razers en zonas vulnerables.'),
P('<b>Lo que esto significa:</b> mantenerse lejos del cañón no basta. La ruta tiene que estar fuera del polígono federal completo. Los vértices vienen en el decreto (UTM zona 13), pero la red de esta sesión no permitió descargarlo. El siguiente paso es obtener el shapefile de CONANP o el PDF del DOF y sobreponerlo a este trazo.',AL),
P('4. Marco legal para operar fuera del ANP',H2),
tbl([['Tema','Qué pide','Quién'],
['Uso de la tierra','Acuerdo de asamblea ejidal con quórum calificado para dar uso a tierras comunes. Contrato de hasta 30 años (Ley Agraria, arts. 23 y 45)','Ejido dueño del terreno'],
['Impacto ambiental','Si se usan solo brechas existentes, probablemente basta un trámite estatal o municipal (por confirmar). Si hay desmonte o apertura, se necesita MIA (LGEEPA art. 28) y cambio de uso de suelo forestal (LGDFS art. 93: el matorral cuenta como terreno forestal)','SRNyMA Durango / SEMARNAT'],
['Zona federal del Nazas','No tocar el cauce ni su zona federal sin concesión','CONAGUA / SEMARNAT'],
['Ruido y emisiones','NOM-080 y NOM-082-SEMARNAT-1994 (ruido de motos), NOM-048-SEMARNAT-1993 (emisiones)','Operador de la ruta'],
['Especies en riesgo','La zona tiene unas 54 a 57 especies en la NOM-059: rapaces (aguililla negra menor, gavilán de Cooper), biznagas, noa (<i>Agave victoriae-reginae</i>). Hay que confirmar con CONANP la temporada de anidación','CONANP'],
['Seguridad','Carta responsiva, seguro de visitantes y ruta de rescate','Ejido / operador'],
],[3.2*cm,9.6*cm,4.2*cm]),
P('5. Derrama económica estimada (supuestos, no datos)',H2),
tbl([['Concepto (escenario base: 40 vehículos por fin de semana, 2 personas cada uno)','Por fin de semana','Por mes (4 fines)'],
['Cuota de acceso: $150 por vehículo','$6,000','$24,000'],
['Comida en paraderos: $150 por persona (ingreso bruto de las familias)','$12,000','$48,000'],
['Renta de 5 puestos: $200 por día, 2 días','$2,000','$8,000'],
['Camping: 8 personas a $100','$800','$3,200'],
['<b>Total derrama</b>','<b>$20,800</b>','<b>aprox. $83,000</b>'],
],[10.5*cm,3.2*cm,3.3*cm]),
P('Escenario alto (120 vehículos por fin de semana): unos $250,000 al mes de derrama. Referencias: Dunas de Bilbao (ejido en Viesca) cobra entre $30 y $50 por persona y entre $50 y $80 por noche de camping; el Coahuila 1000 Desert Rally dejó entre 50 y 75 millones de pesos. Los riesgos que pueden anular estos números son el conflicto con CONANP si la ruta toca el ANP, los accidentes sin seguro y el calor extremo de verano.',SM),
KeepTogether([P('6. Siguientes pasos',H2),
tbl([['#','Paso','Resultado'],
['1','Conseguir el polígono oficial del ANP federal (CONANP/SIMEC o el DOF del 08-01-2024) y sobreponerlo al trazo','Confirmar que la ruta queda 100% fuera'],
['2','Ubicar en campo Santa Anita y Santo Niño. Las fuentes no dan coordenadas confiables: hay que verificar si Santa Anita (225 hab., aprox. 27 km al NO de Cd. Lerdo) está junto a este circuito','Saber qué comunidades se benefician'],
['3','Recorrido de reconocimiento con GPS (el archivo ruta.gpx va incluido): brechas, cercos, arroyos y fotos','Trazo de campo, versión 2'],
['4','Identificar el ejido dueño (RAN / Padrón e Historial de Núcleos Agrarios) y presentarle el proyecto en asamblea','Carta de intención'],
['5','Consulta previa con SRNyMA Durango y CONANP','Saber qué trámite aplica'],
['6','Opcional: agregar un lazo técnico de 3 a 5 km, solo si se confirma que queda fuera del ANP','Más diversión para los que buscan reto'],
],[0.8*cm,11.2*cm,5*cm])]),
P('7. Datos y fuentes',H2),
P('Imagen: Copernicus Sentinel-2 L2A, escena S2A_13RFJ_20261114 (nubosidad &lt; 0.01%), vía AWS Open Data. Topografía: Copernicus DEM GLO-30. Coordenadas de localidades: extractos de municipiodata.com (Censo 2020), pendientes de verificar con INEGI. Normativa: ficha Ramsar 1747 (rsis.ramsar.org), DOF 08-01-2024 (APRN Ríos y Montañas de la Comarca Lagunera), LGEEPA, LGDFS, Ley Agraria, NOM-059/080/082/048-SEMARNAT, El Siglo de Torreón (2024 y 2026), posta.com.mx. Archivos incluidos: ruta.gpx, ruta.kml (Google Earth) y ruta.geojson en la carpeta datos/.',SM),
]
def foot(c,d):
    c.setFont('Helvetica',7); c.setFillColor(colors.grey); c.drawString(2*cm,1.2*cm,'Circuito El Lomerío · propuesta preliminar · no transitar sin autorización ejidal'); c.drawRightString(19.6*cm,1.2*cm,f'{d.page}')
SimpleDocTemplate(OUT+'ruta-20km-preliminar.pdf',pagesize=letter,leftMargin=2*cm,rightMargin=2*cm,topMargin=1.6*cm,bottomMargin=1.8*cm,title='Circuito off-road El Lomerío',author='Asistente').build(E,onFirstPage=foot,onLaterPages=foot)
print('ok')
