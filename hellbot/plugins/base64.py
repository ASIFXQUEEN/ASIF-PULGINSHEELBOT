import base64

from subprocess import PIPE
from subprocess import run as runapp

from . import *


@hell_cmd(pattern="hash ([\s\S]*)")
@errors_handler
async def gethash(event):
    event = await eor(event, "Processing...")
    hashtxt_ = event.pattern_match.group(1)
    hashtxt = open("hashdis.txt", "w+")
    hashtxt.write(hashtxt_)
    hashtxt.close()
    md5 = runapp(["md5sum", "hashdis.txt"], stdout=PIPE)
    md5 = md5.stdout.decode()
    sha1 = runapp(["sha1sum", "hashdis.txt"], stdout=PIPE)
    sha1 = sha1.stdout.decode()
    sha256 = runapp(["sha256sum", "hashdis.txt"], stdout=PIPE)
    sha256 = sha256.stdout.decode()
    sha512 = runapp(["sha512sum", "hashdis.txt"], stdout=PIPE)
    runapp(["rm", "hashdis.txt"], stdout=PIPE)
    sha512 = sha512.stdout.decode()
    ans = (
        "Text: `"
        + hashtxt_
        + "`\nMD5: `"
        + md5
        + "`SHA1: `"
        + sha1
        + "`SHA256: `"
        + sha256
        + "`SHA512: `"
        + sha512[:-1]
        + "`"
    )
    if len(ans) > 4096:
        hashfile = open("hashes.txt", "w+")
        hashfile.write(ans)
        hashfile.close()
        await event.client.send_file(
            event.chat_id,
            "hashes.txt",
            reply_to=event.id,
            caption="`It's too big, sending a text file instead. `",
        )
        runapp(["rm", "hashes.txt"], stdout=PIPE)
    else:
        await event.reply(ans)
        await event.delete()


@hell_cmd(pattern="b64 (en|de) ([\s\S]*)")
@errors_handler
async def endecrypt(event):
    if event.pattern_match.group(1) == "en":
        lething = str(base64.b64encode(bytes(event.pattern_match.group(2), "utf-8")))[
            2:
        ]
        await event.reply("**Encoded :** \n\n`" + lething[:-1] + "`")
        await event.delete()
    elif event.pattern_match.group(1) == "de":
        lething = str(
            base64.b64decode(
                bytes(event.pattern_match.group(2), "utf-8"), validate=True
            )
        )[2:]
        await event.reply("**Decoded :**\n\n`" + lething[:-1] + "`")
        await event.delete()
    else:
        await eod(event, f"You should check out `{hl}plinfo base64` !!")


CmdHelp("base64").add_command(
  "hash", "<query>", "Finds the md5, sha1, sha256, sha512 of the string when written into a txt file"
).add_command(
  "b64 en", "<query>", "Finds the base64 encoding of the given string"
).add_command(
  "b64 de", "<query>", "Finds the base64 decoding of the given string"
).add_info(
  "Base 64 Encode & Decode!"
).add_warning(
  "✅ Harmless Module."
).add()
