from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 24939720
api_hash = 'ee9c32c9a715cf126cb2aee3ea53bd71'

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("Войдите в Telegram, следуя инструкции ниже.")
    session_string = client.session.save()
    print("Ваш session_string:\n")
    print(session_string)
