import requests
from quart import Quart, render_template, websocket
import os 

WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 5000
app = Quart(__name__)

url = WEBHOOK_URL
data = {}
result = {} 

@app.route("/")
async def index():
    data["embeds"] = [
        {
        "title": "Server monitoring is online!",
        "color": 7440858,
        "description": "",
        "timestamp": "",
        "author": {},
        "image": {
            "url": ""
        },
        "thumbnail": {
            "url": "https://i.imgur.com/kRclrub.gif"
        },
        "footer": {},
        "fields": []
        }
    ]

    result = requests.post(url, json=data, headers={"Content-Type": "application/json"})
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Success!, code {result.status_code}.")
        return {"status":200}

@app.route("/server-start")
async def start():
    data["embeds"] = [
        {
        "title": "Factorio server is up and running!",
        "color": 6749952,
        "description": "",
        "timestamp": "",
        "author": {},
        "image": {
            "url": ""
        },
        "thumbnail": {
            "url": "https://i.imgur.com/P4BZ3cY.gif"
        },
        "footer": {},
        "fields": []
        }
    ]

    result = requests.post(url, json=data, headers={"Content-Type": "application/json"})

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Success!, code {result.status_code}.")
        return {"status":200}

@app.route("/server-stop")
async def stop():
    data["embeds"] = [
        {
        "title": "Factorio server shutting down...",
        "color": 16711680,
        "description": "",
        "timestamp": "",
        "author": {},
        "image": {
            "url": ""
        },
        "thumbnail": {
            "url": "https://i.imgur.com/KAKRiTr.gif"
        },
        "footer": {},
        "fields": []
        }
    ]

    result = requests.post(url, json=data, headers={"Content-Type": "application/json"}) 
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Success!, code {result.status_code}.")
        return {"status":200}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
