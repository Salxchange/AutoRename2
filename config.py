import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "22418774")
    API_HASH  = os.environ.get("API_HASH", "d8c8dab274f9a811814a6a96d044028e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6853799265:AAHAia3VERsC01OlMEcgpNrIgWaC_8mnw1o") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","Roku")     
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://mehtadmphta33:Mehtab1234@cluster0.bfsb3oq.mongodb.net/?retryWrites=true&w=majority")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://telegra.ph/file/3408344d69952d7a739e9.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1966867320').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "Rokubotz") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001870788712"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):

    SEQUENCE_TXT = """𝖳𝗁𝖾 𝖥𝗂𝗅𝖾 𝖲𝖾𝗊𝗎𝖾𝗇𝖼𝗂𝗇𝗀 𝖡𝗈𝗍. 𝖧𝖾𝗋𝖾'𝗌 𝖧𝗈𝗐 𝖳𝗈 𝖴𝗌𝖾:

1. 𝖴𝗌𝖾 𝖳𝗁𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽 /startsequence 𝖳𝗈 𝖡𝖾𝗀𝗂𝗇 𝖠 𝖥𝗂𝗅𝖾 𝖲𝖾𝗊𝗎𝖾𝗇𝖼𝗂𝗇𝗀 𝖯𝗋𝗈𝖼𝖾𝗌𝗌.
2. 𝖲𝖾𝗇𝖽 𝖳𝗁𝖾 𝖥𝗂𝗅𝖾𝗌 𝖸𝗈𝗎 𝖶𝖺𝗇𝗍 𝖳𝗈 𝖲𝖾𝗊𝗎𝖾𝗇𝖼𝖾 𝖮𝗇𝖾 𝖡𝗒 𝖮𝗇𝖾
3. 𝖶𝗁𝖾𝗇 𝖸𝗈𝗎'𝗋𝖾 𝖣𝗈𝗇𝖾 , 𝖴𝗌𝖾 /endsequence 𝖳𝗈 𝖥𝗂𝗇𝗂𝗌𝗁 𝖠𝗇𝖽 𝖦𝖾𝗍 𝖳𝗁𝖾 𝖲𝖾𝗊𝗎𝖾𝗇𝖼𝖾𝖽 𝖥𝗂𝗅𝖾𝗌.
    """
        
    START_TXT = """𝖧𝖾𝗅𝗅𝗈 👋 {}
𝗂 𝖺𝗆 <a href=http://t.me/FuZionX_SD_Bot>𝖥𝗎𝖹𝗂𝗈𝗇𝖷 𝖲𝖣</a>, 𝖠𝗇 𝖠𝗎𝗍𝗈 𝖱𝖾𝗇𝖺𝗆𝖾 𝖡𝗈𝗍,
𝖳𝗁𝖺𝗍 𝖱𝖾𝗇𝖺𝗆𝖾𝗌 𝖠𝗇𝗂𝗆𝖾 𝖥𝗂𝗅𝖾𝗌 𝖳𝗈 𝖳𝗁𝖾 𝖥𝗈𝗋𝗆𝖺𝗍 𝖳𝗈 𝖲𝖾𝗍 . "

𝖳𝗈 𝖲𝖾𝖾 𝖬𝗒 𝖥𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝗌, 𝖴𝗌𝖾 𝖳𝗁𝖾 𝖡𝗎𝗍𝗍𝗈𝗇𝗌 𝖡𝖾𝗅𝗈𝗐"
"""
    
    FILE_NAME_TXT = """
    <u><b>SETUP AUTO RENAME FORMAT</b></u>\n\nUse These Keywords To Setup Custom File Name\n\n➝ episode :- to replace episode number\n➝ quality :- to replace video resolution\n\n‣ <b>Example :</b> /autorename [FZ] High Card S1 - Eepisode [quality] Sub @FZAnime.mkv\n\n‣ <b>Your Current Rename Format :</b> {format_template}
    """
    
    ABOUT_TXT = f"""<b>╭───────────⍟
├🤖 𝖬𝗒 𝗇𝖺𝗆𝖾: <a href=http://t.me/FuZionX_SD_Bot>𝖥𝗎𝖹𝗂𝗈𝗇𝖷 𝖲𝖣</a>
├📕 𝖫𝗂𝖻𝗋𝖺𝗋𝗒: <a href=https://github.com/pyrogram>𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆</a>
├✏️ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾: <a href=https://www.python.org>𝖯𝗒𝗍𝗁𝗈𝗇3</a>
├💾 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾: <a href=https://cloud.mongodb.com>𝖬𝗈𝗇𝗀𝗈𝖣𝖡</a>
├📊 𝖡𝗎𝗂𝗅𝖽 𝖵𝖾𝗋𝗌𝗂𝗈𝗇: `OBI V1.7.0`
├🔗 𝖦𝗂𝗍𝖧𝗎𝖻: <a href=https://github.com/SilentDemonSD>𝖲𝗂𝗅𝖾𝗇𝗍𝖣𝖾𝗆𝗈𝗇𝖲𝖣</a>
├📧 𝖢𝗈𝗇𝗍𝖺𝖼𝗍: <a href=https://telegram.me/MysterySD>𝖲𝗂𝗅𝖾𝗇𝗍𝖣𝖾𝗆𝗈𝗇</a>
╰───────────────⍟ 
"""

    
    THUMB_TXT = """ • /start the bot and send any photo to automatically set the thumbnail.
• /del_thumb to delete your old thumbnail.
• /view_thumb to view your current thumbnail."""

    PREMIUM_TXT = """𝖢𝗈𝗆𝗂𝗇𝗀 𝖲𝗈𝗈𝗇"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @rokubotz🙏🥲
    COMMANDS_TXT = """🌌 How To Set Thumbnail
  
• /start the bot and send any photo to automatically set the thumbnail.
• /del_thumb to delete your old thumbnail.
• /view_thumb to view your current thumbnail.

📑 How To Set Custom Caption
• /set_caption - Use this command to set a custom caption.
• /see_caption - Use this command to view your custom caption.
• /del_caption - Use this command to delete your custom caption.
Example: /set_caption 📕 File Name: {filename}
💾 Size: {filesize}
⏰ Duration: {duration}

✏️ How To Rename A File
• Send any file and type the new file name and select the format [document, video, audio].    """

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


