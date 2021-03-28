import numpy as np
import datetime as dt
import cbpro, time, websocket, json
import pandas as pd
import streamlit as st
import dateutil


################################ API ###############################

apiKey = "a736a46415255afe50ea079fe5189d27"
apiSecret = "clGq2k6rrGM2JiyZ5upZBeCkf5p6+NIbYQpJBpDR8r0qCM5BliB/TotWmb+ILBL4JDykw0IyYKNQGdHPrDiNBw=="
passphrase = "lmmd93"
auth_client = cbpro.AuthenticatedClient(apiKey, apiSecret, passphrase)
public_client = cbpro.PublicClient()

####################################################################

btc = "BTC-USD"
eth= "ETH-USD"

try:
    accnts = auth_client.get_accounts()
    for i in accnts:
        bal = float(i['balance'])
        if (bal> 0.0000001):
            print("\n{} : {}\n-----".format(i['currency'], round(bal,10)))

except:
    #st.error("error encountered")
    print("error")
####################################################################


def on_open(ws):
    print("\t === connection opened === \n")

    subscribe_message = {
        "type":"subscribe",
        "channels": [
            {
                "name":"ticker",
                "product_ids": [
                    "ALGO-USD"
                ]
            }
        ]
    }
    ws.send(json.dumps(subscribe_message))
    
    
def on_message(ws, message):
    global current_tick, previous_tick

    current_tick=json.loads(message)
    previous_tick = current_tick

    print("\n ==== received tick ==== ")

    tick_datetime_object = dateutil.parser.parse(current_tick['time'])
    tick_dt = tick_datetime_object.strftime("%m/%d/%Y %H:%M")
    print("min: ",tick_datetime_object.minute)
    print("{}  @  {}".format(tick_dt, current_tick['price']))
    time.sleep(5)

    
socket = "wss://ws-feed.pro.coinbase.com"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()

########################################################################
