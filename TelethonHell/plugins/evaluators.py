import asyncio
import io
import os
import sys
import time
import traceback

from TelethonHell.DB.gvar_sql import gvarstat
from . import *


@hell_cmd(pattern="exec(?:\s|$)([\s\S]*)")
async def _(event):
    if gvarstat("USE_EVAL") == "TRUE":
        Config.LOGGER_ID
        cmd = "".join(event.text.split(maxsplit=1)[1:])
        if not cmd:
            return await eod(event, "`What should i execute?..`")
        hell = await eor(event, "`Executing.....`")
        process = await asyncio.create_subprocess_shell(
            cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        _out_ = str(stdout.decode().strip()) + str(stderr.decode().strip())
        try:
            result = await env_safe_clean(_out_, HARMFUL)
        except:
            result = _out_
        helluser = await event.client.get_me()
        if helluser.username:
            curruser = helluser.username
        else:
            curruser = "@Its_HellBot"
        uid = os.geteuid()
        if uid == 0:
            cresult = f"`{curruser}:~#` `{cmd}`\n`{result}`"
        else:
            cresult = f"`{curruser}:~$` `{cmd}`\n`{result}`"
        final_output = f"**Command :**  `{cmd}`\n**Result :** \n{cresult}"
        if len(final_output) > 4092:
            await eor(
                hell,
                final_output,
                deflink=True,
                linktext=f"**Command:** \n`{cmd}` \n\n**Pasted:** ",
            )
        else:
            await hell.edit(final_output)
    else:
        await eod(
            event,
            f"**Eval Is Disbaled !!** \n\n__Do__ `{hl}svar USE_EVAL TRUE` __to enable eval commands.__",
        )


@hell_cmd(pattern="eval(?:\s|$)([\s\S]*)")
async def _(event):
    if gvarstat("USE_EVAL") == "TRUE":
        cmd = "".join(event.text.split(maxsplit=1)[1:])
        if not cmd:
            return await eod(event, "`What should i run ?..`")
        hellevent = await eor(event, "`Running ...`")
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
        try:
            await aexec(cmd, event)
        except Exception:
            exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"
        final_output = f"•  Eval : \n`{cmd}` \n\n•  Result : \n`{evaluation}` \n"
        final_output2 = f"**•  Eval :** \n`{cmd}` \n\n**•  Result :** \n`{evaluation}` \n"
        if len(final_output2) > 4092:
            await eor(
                hellevent,
                final_output,
                deflink=True,
                linktext=f"**•  Eval :** \n`{cmd}` \n\n**Pasted:** ",
            )
        else:
            await eor(
                hellevent,
                final_output,
                deflink=True,
                linktext=f"{final_output2} \n\n**Also Pasted** ",
            )
    else:
        await eod(
            event,
            f"**Eval Is Disbaled !!** \n\n__Do__ `{hl}svar USE_EVAL TRUE` __to enable eval commands.__",
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


@hell_cmd(pattern="bash ([\s\S]*)")
async def _(event):
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    time.time() + PROCESS_RUN_TIME
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY :**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "bashed.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )
            await event.delete()
    await eor(event, output)


CmdHelp("evaluators").add_command(
    "eval", "<expr>", "Execute a python script", "eval print('Hello World.')"
).add_command(
    "exec", "<command>", "Execute a Terminal command on HellBot server and shows details"
).add_command(
    "bash", "<query>", "Bash your codes on linux and gives the output in current chat"
).add_info(
    "Evaluating Modules."
).add_warning(
    "🚫 Don't Execute Commands Unknowingly."
).add()
