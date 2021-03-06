

import websocket
destUri = "127.0.0.1:9080";
# X_API_KEY = "17254faec6a60f58458308763";
# FEED_ID = "65"
print("start")
def on_message(ws, message):
 print (message)
def on_error(ws, error):
 print (error)
def on_close(ws):
 print ("### closed ###")
def on_open(ws):
 print ("### opened ###")
 msg = {"message": "config_get"}
#  "{\"headers\":{\"X-ApiKey\":\""+ X_API_KEY
# +"\"},\"method\":\"subscribe\", \"resource\":\"/feeds/" +
# FEED_ID + "\"}";
 print ("Sending message...")
 print (msg)
 ws.send(msg)

ws = websocket.WebSocketApp(destUri,
 on_message = on_message,
 on_error = on_error,
 on_close = on_close)
ws.on_open = on_open
ws.run_forever()
