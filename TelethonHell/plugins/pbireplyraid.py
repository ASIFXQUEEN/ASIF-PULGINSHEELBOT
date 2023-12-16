import asyncio
import random

from . import *

RAID_STR = [
"🥹ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਬੱਲਾ ਤੇਰੀ ਭੈਣ ਦਾ ਫੁੱਦਾ ਮਾਰੇ ਗਰੁੱਪ ਦਾ ਮੇਂਬਰ ਕੱਲਾ ਕੱਲਾ😭",
"😈ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਆਲੂ ਪਿਓ ਤੇਰਾ ਟੈਮਪੂ ਮਾਂ ਤੇਰੀ ਚਾਲੂ😈",
"🥵ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਫੂਸਾ ਮੇਰਾ ਡੈਡੀ ਤੇਰੀ ਬੁੰਡ ਮਾਰੇ ਮੈ ਮਾਰਾਂ ਤੇਰੀ ਭੈਣ ਦਾ ਘੁਸਾ👅",
"🥵ਵਾਰੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਸ਼ੇਮਪੂ ਮਾਂ ਤੇ bhen ਤੇਰੀ ਸਿੱਰੇ ਦੀ ਟੈਕਸੀ ਤੂੰ ਤੇ ਤੇਰਾ ਪਿਓ ਪਿੰਡ ਦੇ ਮਸ਼ਹੂਰ ਟੈਮਪੂ👅",
"😈ਵਾਰੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਵੱਟਾ ਮਾਂ ਤੇ ਤੇਰੀ ਭੈਣ ਦੇ ਲੁੱਲਾ ਪਾਵਾ ਤੇਰਾ ਪਿਓ ਥੱਲੋ ਦੀ ਚੁੰਗੇ ਮੇਰਾ ਟੱਟਆ👅",
"🥺ਵਾਰੀ ਵਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਅੰਬਾ ਤੇਰੀ ਮਾਂ ਦੇ ਸ਼ੋਲ਼ੇ ਚ ਮਾਰਾਂ 90 ਗਜ ਦਾ ਟੰਬਾ😭",
"🥹ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਟੰਬਾ ਤੇਰੀ ਮਾਂ ਤੇ ਚੜਜੇ ਮੇਰਾ ਪਿਓ ਤੇ me ਤੇਰੀ ਬੁੰਡ ਚ ਮਾਰਾਂ ਖਮਬਾ😈",
"😭ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਫੇਬੂ ਤੇਰੀ ਮਾਂ ਦਾ ਫੁੱਦੜਾ ਮਾਰੇ ਸਾਡੇ ਪਿੰਡ ਵਾਲਾ ਬਿੱਕਰ ਸੇਬੂ🥵",
"👅ਬੜੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਲਾਲੀ ਤੇਰੇ ਪਿਓ ਦੇ ਮਾਰਾਂ ਲੁੱਲਾ ਤੇਰੀ ਭੈਣ ਦੇ ਸ਼ੋਲ਼ੇ ਚ ਟਰਾਲ਼ੀ👅",
"🥵ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਏ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਬੈਡ ਤੇਰੀ ਮਾਂ ਤੇ ਤੇਰੇ ਪਿਓ ਦੀ ਪੱਟਾਂ ਬੁੰਡ ਤੇਰੀ ਭੈਣ ਦੇ ਫੁੜਦੇ ਚ ਸ਼ੈੱਡ😭",
"🥹ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਰੀਡ ਆਵਦੀ ਮਾਂ ਤੇ ਭਵਨ ਕਰ ਨੰਗੀ ਜੇ ਮੈਚ ਨੀ ਹੁੰਦੀ ਸਪੀਡ🥹",
"🥵ਕਹਿੰਦੇ ਆਰ ਟਾਂਗਾ ਪਾਰ ਟਾਂਗਾ ਵਿਚ ਟਾਂਗਾ ਦੇ ਟੋਏ ਤੇਰੀ ਭੈਣ ਦਾ ਫੁੱਦਾ ਮਾਰਾਂ ਤੇਰਾ ਪਿਓ ਕੋਲ ਖੜਾ ਕਰੇ ਓਏ ਓਏ🥹"
"👅ਕਹਿੰਦੇ ਆਰ ਟਾਂਗਾ ਪਾਰ ਟਾਂਗਾ ਵਿਚ ਟਾਂਗਾ ਦੇ ਹੁਲ ਤੇਰੀ ਮਾਂ ਦੀ ਮਾਰਾਂ ਸ਼ੋਲੀ ਤੇਰੀ ਭੈਣ ਦੇ ਫੁੜਦੇ ਚ 10 ਗਜ ਦਾ ਲੁੱਲ🥵",
"😭ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦੀ ਤੋਰੀ ਪਿਓ ਤੇਰਾ ਸ਼ੱਕਾ ਤੇਰੀ ਮਾਂ ਦੀ ਫੁੱਦੀ ਚ ਬਹੁਤ ਵੱਡੀ ਮੋਰੀ😭",
"🥵ਬਾਰੀ ਬਰਸੀ ਖੱਟਣ ਗਿਆ ਸੀ ਖੱਟ ਕੇ ਲਿਆਂਦਾ ਕੱਮ ਤੇਰਾ ਪਿਓ ਲਾਵੇ ਚੁੱਪੇ ਤੇਰੀ ਭੈਣ ਦੇ ਫੁੜਦੇ ਚ ਡਰੱਮ👅",
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

@hell_cmd(pattern="bireplyraid(?:\s|$)([\s\S]*)")
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
        event = await eor(event, "pbi Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"pbi Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "pbi Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"pbi Reply Raid has been activated on {username}")


@hell_cmd(pattern="dpbireplyraid(?:\s|$)([\s\S]*)")
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
        await event.edit(f"PBI Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await eor(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"PBI Reply Raid has been De-activated on {username}")

CmdHelp("pbireplyraid").add_command(
    "replyraid", None, "Starts pbi reply raid on mentioned user."
).add_command(
    "dpbireplyraid", None, "Stops pbi reply raid on mentioned user."
).add_warning(
    "May get floodwait!"
).add_info(
    "Spammer Module"
).add()
