import telebot
import requests
bot = telebot.TeleBot("BOT API Key")
def extract_arg(arg):
	return arg.split()[1:]

@bot.message_handler(commands=['temp'])
def send_welcome(message):
	try:
		city = extract_arg(message.text)
		if not city:
			payload = {'appid':'OWM API Key', 'q':'Красноярск', 'lang':'ru', 'units':'metric'} # Default city if no city after /temp command
		else:
			payload = {'appid':'OWM API Key', 'q':city, 'lang':'ru', 'units':'metric'} # 
		p = requests.get('https://api.openweathermap.org/data/2.5/weather', params=payload)
		answer = eval(p.content.decode('utf-8'))
		p_city = answer.get('name')
		temp = answer.get('main').get('temp')
		wind = answer.get('wind', {}).get('speed')
		pressure = answer.get('main').get('pressure')
		msg = '{}: {} С, ветер {} м/сек, давление {} hPa'.format(p_city, round(temp), round(wind), pressure)
		bot.reply_to(message, msg)
	except:
		bot.reply_to(message, 'Поломочка')

print('Bot runnig')
bot.infinity_polling()
