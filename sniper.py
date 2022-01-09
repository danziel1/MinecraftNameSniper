import requests
import time
import string
import random

length = 3 # set to the length of the ign that you want to snipe

webhook = 'Webhook URL'




while True:
    name = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits)
    for _ in range(length))
    try:
        getuuid = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{name}').json()
        uuid = getuuid['id']
        print(f"> {name} is invalid")
    except:
        print(f"> {name} is valid")
        data = {
    "content" : name
}
        result = requests.post(webhook, json = data)
    time.sleep(1.1) # Keep above 1.0 to avoid rate limits
