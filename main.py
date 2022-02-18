import bot, editaImagen, generaImagen, time

try:
	imagen=generaImagen.genera()
	print("imagen generada")
	editaImagen.agregaTexto("Aceituna", imagen)
	print("imagen editada")
	bot.publicaImagen()
	print("imagen publicada")
	time.sleep(15)


except Exception as e:
	print(e)
	time.sleep(15)
