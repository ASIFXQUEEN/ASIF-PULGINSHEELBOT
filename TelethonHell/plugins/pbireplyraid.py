import asyncio
import random

from . import *

RAID_STR = [
"🥹मादरचोद भोसदिके-सड़ी हुई बिल्ली से पैदा हुआ",
"😈बहन चोद बेटी चोद भाधवा- दलाल",
"🥵चोदू- साला चुटिया- साला, कमीने👅",
"🥵गधा गांडू बाकलैंड- बेवकूफ",
"😈लौड़ा हिजड़ा लंड👅",
"🥺रंडी- पतुरिया साला कुत्ता",
"🥹टाटी- छी कामिना😈",
"चूत के पसीने में तले हुए भजिए",
"👅चूत का ढक्कन चुटिया का भेजा घास खाने गया है",
"🥵चूत मारी योनि के बाल",
"🥹चिपकली के झाट के बाल छिपकली के जघन के बालों का पसीना🥹",
"🥵चिपकली के गांड के पसीने चिपकली के चूत के पसीने🥹"
"👅चिपकली की भीगी चूत वेश्या के स्तन के निपल के बाल की जूँ",
"अपने आप को मुट्ठी भर वीर्य में डुबो देना कुन्त्मामा- योनि अंकल",
"🥵तेरी माँ का भरोसा अपनी गांड में मुट्ठी डालो जाओ और अपना लंड चूसो जाओ और अपनी बहन की गेंदों को चूसो अबला नारी तेरा बबल भारी👅",
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

@hell_cmd(pattern="hirraid(?:\s|$)([\s\S]*)")
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
        event = await eor(event, "hindi Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"hindi Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "hindi Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"hindi Reply Raid has been activated on {username}")


@hell_cmd(pattern="dhirraid(?:\s|$)([\s\S]*)")
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
        event = await eor(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"hindi Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"hindi Reply Raid has been De-activated on {username}")

CmdHelp("hindireplyraid").add_command(
    "hirraid", None, "Starts hindi reply raid on mentioned user."
).add_command(
    "dhirraid", None, "Stops hindi reply raid on mentioned user."
).add_warning(
    "May get floodwait!"
).add_info(
    "Spammer Module"
).add()
