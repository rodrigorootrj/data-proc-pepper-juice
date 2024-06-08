import sys
sys.path.append("..")
import telepot
import configparser, os
config = configparser.ConfigParser()
config.read_file(open('./etc/configuracao.conf'))
telegram_group = config.get('telegram_group', 'group')
token_telegram = config.get('token_telegram', 'token_key')
class Telegram:
    def sendMessage(text):
        # Insira seu token do bot aqui
        token = token_telegram
        # Insira o ID do canal aqui
        canal_id = telegram_group
        # Crie um objeto da classe `Bot`
        bot = telepot.Bot(token)
        # Envie a mensagem para o canal
        mensagem = text
        bot.sendMessage(canal_id, mensagem)
        return 200    