import numpy as np
import datetime as dt
import cbpro, time
import pandas as pd

################################ API ###############################

apiKey = "a736a46415255afe50ea079fe5189d27"
apiSecret = "clGq2k6rrGM2JiyZ5upZBeCkf5p6+NIbYQpJBpDR8r0qCM5BliB/TotWmb+ILBL4JDykw0IyYKNQGdHPrDiNBw=="
passphrase = "lmmd93"
auth_client = cbpro.AuthenticatedClient(apiKey, apiSecret, passphrase)
public_client = cbpro.PublicClient()

####################################################################

btc = "BTC-USD"
eth= "ETH-USD"


def get_current_rsi():
    current_close=0
    prev_close=0
    diff=0
    over="------"
    global xx
    
    print("Current Price:\t${}\n".format(public_client.get_product_ticker(product_id=coin)['price']))
    for x in hst[:30]:
        date = dt.datetime.fromtimestamp(x[0])
        print("Time: {}\tHigh: {}\tLow: {}\tClose: {}".format(date,x[2], x[1], x[4]))
        closes.insert(0,x[4])
    
    for a in closes:
        current_close = a
        diff = round(current_close-prev_close,2)
        if diff > 0 :
            pos_chng.append(diff)
        if diff < 0 :
            neg_chng.append(diff)
        prev_close=current_close
    
    df = pd.DataFrame(hst[:30])
    df.columns=["Time", "Low", "High", "Open", "Close", "Volume"]
    #print(df)
    xx = range(len(closes))
    
    avg_gain=round((sum(pos_chng[1:])/len(pos_chng)),2)
    avg_loss=round(-(sum(neg_chng[1:])/len(neg_chng)),2)
    print("Average Gain: {}\nAverage Loss: {}".format(avg_gain, avg_loss))
    RS = avg_gain/avg_loss
    RSI = 100 - (100/(1+RS))
    if RSI >72:
        over="overbought - sell"
    elif RSI < 28:
        over="oversold - buy"
    else :
        print("Neither overbought or oversold")
    return("RSI:\t{}".format(round(RSI,2)))
    print(over)


##############################################################################



