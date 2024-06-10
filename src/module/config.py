import sys
sys.path.append("..")
import configparser, os
config = configparser.ConfigParser()
config.read_file(open('./etc/configuracao.conf'))
telegram_group = config.get('telegram_group', 'token_group_key')
token_telegram = config.get('token_telegram', 'token_telegram_key')

