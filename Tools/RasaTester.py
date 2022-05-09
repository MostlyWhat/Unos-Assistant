import requests

sender = input("What is your name?\n")

while True:
	message = input("What's your message?\n")

	r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})

	for i in r.json():
		bot_message = i['text']
		print(f"{bot_message}")
