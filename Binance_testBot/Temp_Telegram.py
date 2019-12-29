from telethon import TelegramClient, sync, events
from threading import Thread


class Telegram(Thread):

	def __init__(self, api_id, api_hash, even_thandler):
		Thread.__init__(self)

		self.even_thandler = even_thandler
		self.api_id = api_id
		self.api_hash = api_hash
		self.client = TelegramClient('session_name', self.api_id, self.api_hash)
		pass

	def run(self):

		# @client.on(events.NewMessage(chats='https://t.me/CQSScalpingFree'))
		@self.client.on(events.NewMessage())
		def normal_handler(event):
			mess_mess=event.message.text
			mess_name=event.message.chat.username
			mess_date=event.message.date

			mess_lines = mess_mess.split('\n')
			if mess_lines[1][:3] == 'BUY' and mess_lines[0].find('BINANCE')!=-1:
				self.symbol = mess_lines[0].split('`')[1][1:]
				s = self.symbol.split('_')
				self.basecurrence = s[0]
				self.quotecurrence = s[1]
				self.buy = float(mess_lines[1].split('`')[1])
				self.target = float(mess_lines[2].split('`')[1])

				self.even_thandler(self, self.basecurrence, self.quotecurrence, self.buy, self.target)

		self.client.start()
		self.client.run_until_disconnected()

