import random
def genera():
	aleatorio1=str(random.randrange(100000))
	aleatorio2=str(random.randrange(150,1000))
	aleatorio3=str(random.randrange(150,1000))
	link="https://picsum.photos/seed/" +aleatorio1 +"/" +aleatorio2 +"/" +aleatorio3
	print(link)
	#https://picsum.photos/seed/pfshfdef/600/400
	return link
