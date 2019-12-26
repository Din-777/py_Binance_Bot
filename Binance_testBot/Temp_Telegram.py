from telethon import TelegramClient, sync, events

api_id = 1131638
api_hash = '404de1876f2b88c0edd8b97c055cbdcf'

client = TelegramClient('session_name', api_id, api_hash)

# @client.on(events.NewMessage(chats='https://t.me/CQSScalpingFree'))
@client.on(events.NewMessage())
async def normal_handler(event):
	mess_mess=event.message.to_dict()['message']
	mess_name=event.message.chat.to_dict()['username']
	mess_date=event.message.to_dict()['date']
	
	print(mess_date.strftime("%d-%m-%Y %H:%M"))
	print(mess_name)
	print(mess_mess+"\n\n")

client.start()
client.run_until_disconnected()
