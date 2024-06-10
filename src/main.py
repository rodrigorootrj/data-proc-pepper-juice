import sys
sys.path.append(".")
#from google.cloud import storage
## LOCAL
##
from module.dataasset import Seller
##

def seller_crypto_bot(event,context):  
    Seller.seller_crypto_bot()
seller_crypto_bot(1,2)    