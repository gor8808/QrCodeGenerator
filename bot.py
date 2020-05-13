import telebot
from telebot import types
import config
from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
import qrcode
import uuid

bot = telebot.TeleBot(config.TOKEN)
print("Start working")
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.text[0] == '/':
		pass
	else:
		# bot.send_message(message.chat.id,downloadType)
		print(message.chat.id)
		fileName = ".\\QrCodes\\QRCodeGenerator_GAIBot_" + str(uuid.uuid4())
		img = qrcode.make(message.text)   
		img.save(fileName+'.bmp')
		image = open(fileName + ".bmp","rb")

		bot.send_photo(message.chat.id,image)	
		# bot.send_message(516342699,str(message.chat.id) + " user use qr generator with this text -- " + message.text)
		bot.send_message(message.chat.id,"Welcome to Qr Code Generator bot. \nJust send me text and i will reply you your Qr code .\nG.A.I. \n\nԲարի գալուստ QR կոդ ստեղծող բոտ։ \nՈւղարկեք ինձ տեքստ ,և ես ձեզ պատասխան նամակում կուղարկեմ ծեր QR կոդը։ \nG.A.I.")

bot.polling()