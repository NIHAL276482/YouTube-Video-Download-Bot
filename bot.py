# UNKNOWN YT| @ILOVETHATBREATHS | Sk and tnt | 

# [⚠️ Do not change this repo link ⚠️] :- 



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.28668719, 
    api_hash=Config.f55a34ede55fae170c2d89a782d06cdb, 
    bot_token=Config.8011240970:AAHazVuPwHd-a5AljyDdjj1om1Tn0Mo1OtI,
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
