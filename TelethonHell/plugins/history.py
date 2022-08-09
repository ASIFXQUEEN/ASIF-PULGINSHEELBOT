from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import *


@hell_cmd(pattern="history(?:\s|$)([\s\S]*)")
async def _(hellevent):
    if not hellevent.reply_to_msg_id:
        await parse_error(hellevent, "No user mentioned!")
        return
    reply_message = await hellevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(hellevent, "Need actual users. Not Bots")
        return
    hell = await eor(hellevent, "Checking...")
    async with hellevent.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
            response3 = await conv.get_response()
        except YouBlockedUserError:
            await parse_error(hellevent, "__Unblock @Sangmatainfo_bot and try again.__", False)
            return
        if response1.text.startswith("Name History"):
            await hell.edit(response1.text)
            await hellevent.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        elif response2.text.startswith("Name History"):
            await hell.edit(response2.text)
            await hellevent.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        elif response3.text.startswith("Name History"):
            await hell.edit(response3.text)
            await hellevent.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        else:
            await hell.edit("No Records Found !")


@hell_cmd(pattern="unh(?:\s|$)([\s\S]*)")
async def _(hellevent):
    if not hellevent.reply_to_msg_id:
        await parse_error(hellevent, "No user mentioned.")
        return
    reply_message = await hellevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eod(hellevent, "Need actual users. Not Bots")
        return
    hell = await eor(hellevent, "Checking...")
    async with hellevent.client.conversation(chat) as conv:
        try:
            first = await conv.send_message(f"/search_id {victim}")
            response1 = await conv.get_response()
            response2 = await conv.get_response()
            response3 = await conv.get_response()
        except YouBlockedUserError:
            await parse_error(hellevent, "__Unblock @Sangmatainfo_bot and try again.__", False)
            return
        if response1.text.startswith("Username History"):
            await hell.edit(response1.text)
            await hellevent.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        elif response2.text.startswith("Username History"):
            await hell.edit(response2.text)
            await hellevent.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        elif response3.text.startswith("Username History"):
            await hell.edit(response3.text)
            await hellevent.client.delete_messages(
                conv.chat_id, [first.id, response1.id, response2.id, response3.id]
            )
        else:
            await hell.edit("No Records Found !")


CmdHelp("history").add_command(
    "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
    "unh", "<reply to user>", "Fetches the Username History of replied users."
).add_info(
    "Telegram Name History"
).add_warning(
    "✅ Harmless Module."
).add()
