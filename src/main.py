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
from module.dataasset import Seller
##
import time
import logging

def seller_crypto_bot(event,context):
    logging.INFO('STARTING seller_crypto_bot')
    Seller.seller_crypto_bot()