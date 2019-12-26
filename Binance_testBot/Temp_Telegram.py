from telethon import TelegramClient, sync, events

class Telegram(object):

	def __init__(self, api_id, api_hash):
		self.api_id = api_id
		self.api_hash = api_hash
		self.client = TelegramClient('session_name', self.api_id, self.api_hash)

		# @client.on(events.NewMessage(chats='https://t.me/CQSScalpingFree'))
		@self.client.on(events.NewMessage())
		async def normal_handler(event):
			mess_mess=event.message.to_dict()['message']
			mess_name=event.message.chat.to_dict()['username']
			mess_date=event.message.to_dict()['date']
	
			print(mess_date.strftime("%d-%m-%Y %H:%M"))
			print(mess_name)
			print(mess_mess+"\n\n")

		self.client.start()
		self.client.run_until_disconnected()

		pass

tele = Telegram(1131638, '404de1876f2b88c0edd8b97c055cbdcf')


