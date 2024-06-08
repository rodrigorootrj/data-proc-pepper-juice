import sys
sys.path.append(".")
import pandas as pd
#from google.cloud import storage
## LOCAL
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from module.telegram import Telegram
##
from lib.config import *
from lib.price import preco
##
import time

def seller_crypto_bot(event,context):
    url = 'you-url-googledocs'#please, formate you url before.
    df = pd.read_csv(url)
    size = len(df) 
    objeto_tokens_v2 = {"data":None}
    slices = []
    conunter = 0
    for x in range(0,size):
        worker = int(df.loc[x]['gas'])
        stake = df.loc[x]['stake']
        price = df.loc[x]['price'] 
        stake_id = df.loc[x]['id'] 
        if worker == 0:
            conunter = conunter + 1 
            aux = {'id': conunter,'token' : 'token_pepe','stake' : stake,'price' : price,'stake_id':stake_id}
            slices.append(aux)
    objeto_tokens_v2['data']  = slices    
    var = objeto_tokens_v2
    size = 0
    size = len(var['data'])
    print(size)
    for x in range(0,size):
        token = var['data'][x]['token']
        stake = var['data'][x]['stake']
        price = var['data'][x]['price']
        aux = 'Dear, please buy the token {} a stake of ${} at price:{}'.format(token,stake,price)
        Telegram.sendMessage(aux)
        time.sleep(0.5)
    return 200
#seller_crypto_bot('event','context')