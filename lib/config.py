import sys
sys.path.append(".")
import configparser, os
config = configparser.ConfigParser()
config.read_file(open('./key/configuracao.conf'))
##
token_key = config.get('token_coinmarketcap', 'token_key')