import sys
sys.path.append(".")
import configparser, os
config = configparser.ConfigParser()
config.read_file(open('./etc/configuracao.conf'))
telegram_group = config.get('telegram_group', 'group')
token_telegram = config.get('token_telegram', 'token_telegram_key')
##
token_key = config.get('token_coinmarketcap', 'token_coinmarketcap_key')
ds_url = config.get('default', 'data_sheet')