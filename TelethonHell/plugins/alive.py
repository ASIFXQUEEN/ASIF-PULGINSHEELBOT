import datetime
import random
import time
from unicodedata import name

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from TelethonHell.DB.gvar_sql import gvarstat, addgvar
from TelethonHell.plugins import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🎈𝐌𝐈𝐒𝐒𝐐𝐔𝐄𝐄𝐍 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🎈</i></b>

<b><i> 𝐎𝐖𝐍𝐄𝐑:</i></b> : 『 {hell_mention} 』
╭──────────────
┣─ <b>»𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍:</b> <i>{telethon_version}</i>
┣─ <b>»𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑:</b> <i>{hellbot_version}</i>
┣─ <b>»𝐒𝐔𝐃𝐎:</b> <i>{is_sudo}</i>
┣─ <b>»𝐔𝐏𝐓𝐈𝐌𝐄:</b> <i>{uptime}</i>
┣─ <b>»𝐏𝐈𝐍𝐆:</b> <i>{ping}</i>
╰──────────────
<b><i>»»» <a href='https://t.me/ARAME9'>𝐌𝐈𝐒𝐒𝐐𝐔𝐄𝐄𝐍 𝐁𝐎𝐓</a> «««</i></b>

<b><i>⛧ <a href='https://t.me/ASHIF903'>✦𝑺𝑻𝑹𝑨𝑵𝑮𝑬𝑹✦</a> ⛧</i></b>

<b><i>⛧ <a href='https://t.me/ASHIF903'>✦𐏓 𝐀𝐒𝐈𝐅🦅⃕⃔</a> ⛧</i></b>
"""

msg = """{}\n
<b><i>🏅𝑺𝑻𝑹𝑨𝑵𝑮𝑬𝑹 𝑩𝑶𝑻 𝑺𝑻𝑨𝑼𝑻𝑺🏅</b></i>
<b>𝑻𝑬𝑳𝑬𝑻𝑯𝑶𝑵 ≈</b>  <i>{}</i>
<b>𝑺𝑻𝑹𝑨𝑵𝑮𝑬𝑹 ≈</b>  <i>{}</i>
<b>𝑼𝑷𝑻𝑰𝑴𝑬 ≈</b>  <i>{}</i>
<b>𝑨𝑩𝑼𝑺𝑬 ≈</b>  <i>{}</i>
<b>𝑺𝑼𝑫𝑶 ≈</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@hell_cmd(pattern="alivetemp$")
async def set_alive_temp(event):
    hell = await eor(event, "`Fetching template ...`")
    reply = await event.get_reply_message()
    if not reply:
        alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
        to_reply = await hell.edit("Below is your current alive template 👇")
        await event.client.send_message(event.chat_id, alive_temp, parse_mode=None, link_preview=False, reply_to=to_reply)
        return
    addgvar("ALIVE_TEMPLATE", reply.text)
    await hell.edit(f"`ALIVE_TEMPLATE` __changed to:__ \n\n`{reply.text}`")


@hell_cmd(pattern="alive$")
async def _(event):
    start = datetime.datetime.now()
    userid, hell_user, hell_mention = await client_id(event, is_html=True)
    hell = await eor(event, "`Ruk Jra Sabar Karo 🫴🥺❤️‍🩹`")
    reply = await event.get_reply_message()
    uptime = await get_time((time.time() - StartTime))
    name = gvarstat("ALIVE_NAME") or hell_user
    alive_temp = gvarstat("ALIVE_TEMPLATE") or ALIVE_TEMP
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://telegra.ph/file/eb3d0c67ac1c3b04849a3.jpg"
    end = datetime.datetime.now()
    ping = (end - start).microseconds / 1000
    alive = alive_temp.format(
        hell_mention=hell_mention,
        telethon_version=telethon_version,
        hellbot_version=hellbot_version,
        is_sudo=is_sudo,
        uptime=uptime,
        ping=ping,
    )
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=alive,
        reply_to=reply,
        parse_mode="HTML",
    )
    await hell.delete()


@hell_cmd(pattern="shivop$")
async def hell_a(event):
    userid, _, _ = await client_id(event)
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>»» 𝐌𝐈𝐒𝐒𝐐𝐔𝐄𝐄𝐍 𝐁𝐎𝐓 𝐈s 𝐀ʟɪᴠᴇ ««</b>"
    try:
        hell = await event.client.inline_query(Config.BOT_USERNAME, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == userid:
            await event.delete()
    except (noin, dedbot):
        await eor(
            event,
            msg.format(am, telethon_version, hellbot_version, uptime, abuse_m, is_sudo),
            parse_mode="HTML",
        )


CmdHelp("alive").add_command(
    "alive", None, "Shows the default Alive message."
).add_command(
    "shivop", None, "Shows inline Alive message."
).add_warning(
    "✅ Harmless Module"
).add()
