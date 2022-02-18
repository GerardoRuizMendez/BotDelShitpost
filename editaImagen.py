from PIL import Image, ImageFont, ImageDraw
from urllib.request import urlopen

def agregaTexto(texto, imagen):
	imagen=Image.open(urlopen(imagen))
	points=int(imagen.size[0]*6/100) #tamaño de la fuente
	
	fuente=ImageFont.truetype("Recursos/fuente.ttf",points)
	
	#fuente.getsize_multiline("a",stroke_width=4)
	anchoFuente=fuente.getsize(texto)[0]
	altoFuente=fuente.getsize(texto)[1]

	x=imagen.size[0]/2 - anchoFuente/2
	y=imagen.size[1]*9/10 - altoFuente/2

	edicion=ImageDraw.Draw(imagen)
	edicion.text((x,y), texto, "#000", font=fuente, stroke_width=3,stroke_fill="#FFF")
	imagen.save("Resultados/nueva.png")
	imagen.show()
