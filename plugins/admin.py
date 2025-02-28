import re, asyncio, time, shutil, psutil, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import *
from info import BOT_START_TIME, ADMINS
from utils import humanbytes  


@Client.on_message(filters.private & filters.command("status") & filters.user(ADMINS))          
async def stats(bot, update):
    currentTime = time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - BOT_START_TIME))
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    ms_g = f"""<b><u>👾 ʙᴏᴛ sᴛᴀᴛᴜs 👾</b></u>

<b>ᴜᴘᴛɪᴍᴇ:-</b> <code>{currentTime}</code>
<b>ᴄᴘᴜ ᴜsᴀɢᴇ:-</b> <code>{cpu_usage}%</code>
<b>ʀᴀᴍ ᴜsᴀɢᴇ:-</b> <code>{ram_usage}%</code>
<b>ᴛᴏᴛᴀʟ ᴅɪsᴋ sᴘᴀᴄᴇ:-</b> <code>{total}</code>
<b>ᴜsᴇᴅ sᴘᴀᴄᴇ:-</b> <code>{used} ({disk_usage}%)</code>
<b>ꜰʀᴇᴇ sᴘᴀᴄᴇ:-</b> <code>{free}</code> """

    msg = await bot.send_message(chat_id=update.chat.id, text="__Processing...__", parse_mode=enums.ParseMode.MARKDOWN)         
    await msg.edit_text(text=ms_g, parse_mode=enums.ParseMode.HTML)
    
@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def stop_button(bot, message):
    msg = await bot.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=message.chat.id)       
    await asyncio.sleep(3)
    await msg.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)



