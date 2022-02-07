# AsmSafone
# Radio Player
# Join @AsmSafone


# import logging
from pyrogram import Client, idle

app = Client("RadioPlayer")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED. @MITMUZAFFARPURBOT')
idle()
app.stop()
print('\n>>> USERBOT STOPPED.@MITMUZAFFARPURBOT')
