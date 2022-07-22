import requests
from quart import Quart, render_template, websocket

app = Quart(__name__)

url = "<webhook url>" 
data = {}
result = {}

@app.route("/)
async def start():
    data["content"] = "Factorio monitoring started!"
    data["username"] = "Factorio Bot"

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
    data["content"] = "Factorio is server starting!"
    data["username"] = "Factorio Bot"

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
    data["content"] = "Factorio server is stopping..."
    data["username"] = "Factorio Bot"

    result = requests.post(url, json=data, headers={"Content-Type": "application/json"}) 
    
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Success!, code {result.status_code}.")
        return {"status":200}


if __name__ == "__main__":
    app.run()
