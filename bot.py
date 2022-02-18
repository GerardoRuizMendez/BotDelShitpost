import tweepy


def publicaImagen():
	CONSUMER_KEY=''
	CONSUMER_SECRET=''
	ACCES_KEY=''
	ACCES_SECRET='' #coloca los tokens generados al crear tu cuenta de developer twitter

	auth=tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCES_KEY, ACCES_SECRET)
	api=tweepy.API(auth)
	api.update_with_media("Resultados/nueva.png","Imagen de @usuario")

