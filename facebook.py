import requests
import urllib.parse
import random


class Facebook:
	CLIENT_ID='960467001449769'
	CLIENT_SECRET='885e1d327df02794da46368d148ede6c'

	redirect_url=urllib.parse.quote("https://trial-container-yvkhc.run-ap-south1.goorm.io/face/")

	state = ''.join([str(random.randint(1,7)) for i in range(0,6)])

	code = ''

	auth_endpoint = f"https://www.facebook.com/v6.0/dialog/oauth?client_id={CLIENT_ID}&redirect_uri={redirect_url}&state={state}"

	def get_token():

		access_token_url=f"https://graph.facebook.com/v6.0/oauth/access_token?redirect_uri={redirect_url}&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&code={code}"

		response = requests.get(access_token_url)

		print(response.json())

		input()