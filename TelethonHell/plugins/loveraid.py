import asyncio
import random

from . import *

RAID_STR = [
    "HAYEE MERI JAAN 🤩🤩",
    "MERI JAAN KITNI OSM HAI YAAR 😁🌹🌹😍😍😍",
    "I LOVE YOU MERI JAAN ❤️❤️",
    "MERI JAAN I KISS YOU ❤️😋😊😘😘😘",
    "I MISS YOU JAAN 🥀🥀✨✨",
    "Mat muskurao itna ki Phoolo ko khabar lag jaye Ke wo kare taaref tumhari Aur tumhe unki najar lag jaye",
    "Chand se haseen hai chandni Chandni se haseen hai Raat Raat se haseen hai chand Aur chand se haseen hai aap",
 "You look so beautiful and pretty I feel lucky because you love me I love you now and I’ll always do Because I just can’t live without you",
 "Chand sa tera masoom chehra Tu haya ki ek murat hai Tujhe dekh ke kaliya bhi sharmaaye Tu itni khoobsurat hai", 
 "कैसे करुं बयाँ मै खुबसुरती उसकी मेने तो उसे बिना देखे ही प्यार किया है।", 
 "Mai tumhari sadagi ki kya misal du Is saare jaha me Be misaal ho tum",
 " LOVE YOU JAAN 😁😁🔥🔥😂",
 "I HUG YOU BABY 🤣🤣",
 " I LOVE YOU SO MUCH 🌹💫💖",
 "MADE BY DEV JAAN 😂😂",
 "нello 😍мerι jaan",
 "oye вaвy ѕυno na 😍",
 "ι love υ вaвe😘",
 "тυм нι нo🥺❤️",
 "आप ही के बिना हम क्यों बेचैन हैं",
"आप ही क्यों मेरी जरूरत हैं",
"वहम इतना हसीं नहीं होता",
"वाकई आप खूबसूरत हैं",
"ᴏyᴇ ʜᴏyᴇ ꜱᴀʀᴍᴀ ɢyɪ ᴋᴀᴀ ᴩʜᴏɴᴇ ᴋᴀᴛ ᴅɪ ᴍᴜᴍᴍy ᴀᴀ ɢyɪ ᴋyᴀ 🤣",
" TU MAAN MERI JAAN TUJHE JANE NA DUNGA 🤣🤣✨",
"TUJHE APNI BAHO ME SAJAKE 🤣🤣🤣",
"EK UCHA LMBA KAD DUJA SONI HONI HAD TIJHA TERA RUP CHAM CHAM KR DANI TERE SIVHA DIL ME KOI UTRA THA NHI🤣🤣🤣🤣🌹🌹",
"BS KHAFI HO GYI JHUT KI TARIF🤣🤣🤣",
"HEY HA YOU....YOU ARE SO BEAUTIFUL ✨🌹 I LOVE YOU 🤣🥀🥀🥀✨✨🌹🌹",
"MERI JAAN TUJHE NAZAR NA 🤣LGA JAYE KISI KI 🙄🆘",
" KIN NA SONA TUJHE RAB NE BNAYA KI JI KRE DEKH THA RHU 😂😂🌹🌹❤️❤️😜🤣🤣",
"LAL DUPATTA UD GYA  HAYE MERI BEAUTY SE 🤣🤣😜😜",
"BS BS HO GYI AB JHUTI TARIF JAAN 🤣🤣🤣",
"#LOVE YOU JAAN",
"I WANT YOU 👀BABY",
" UMMMMM MAAA MERI JAAN 😍😘😘😘😘😘",
]

que = {}


@hell_handler()
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RAID_STR)),
            reply_to=event.message.id,
        )

@hell_cmd(pattern="loveraid(?:\s|$)([\s\S]*)")
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await eor(event, "love Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"love has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "love Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"love has been activated on {username}")


@hell_cmd(pattern="dlove(?:\s|$)([\s\S]*)")
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await eor(event, "love De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"love has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "love De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"love has been De-activated on {username}")

CmdHelp("loveraid").add_command(
    "devlove", None, "Starts  love on mentioned user."
).add_command(
    "dlove", None, "Stops  love on mentioned user."
).add_warning(
    "May get floodwait!"
).add_info(
    "Spammer Module"
).add()