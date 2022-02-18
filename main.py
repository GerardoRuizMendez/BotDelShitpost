import bot, editaImagen, generaImagen, time, generaFrase

try:
	imagen=generaImagen.genera()
	print("imagen generada")
	frase=generaFrase.genera()
	editaImagen.agregaTexto("frase", imagen)
	print("imagen editada")
	#bot.publicaImagen()
	print("imagen publicada")
	time.sleep(15)


except Exception as e:
	print(e)
	time.sleep(15)
