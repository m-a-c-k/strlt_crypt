import numpy as np
import datetime as dt
import cbpro, time
import pandas as pd
import streamlit as st

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
            st.write("\n{} : {}\n-----".format(i['currency'], round(bal,10)))

except:
    st.error("error encountered")
    

##############################################################################
