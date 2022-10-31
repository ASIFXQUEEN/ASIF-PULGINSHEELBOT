import functools

from TelethonHell.clients.session import Hell


# forward check
def forwards():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.fwd_from:
                await func(event)
            else:
                pass

        return wrapper

    return decorator


# am i admin?
def iadmin():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            myid = await Hell.get_me()
            myperm = await Hell.get_permissions(event.chat_id, myid)
            if myperm.is_admin:
                await func(event)
            if myperm.is_creator:
                await func(event)
            else:
                await event.edit("I'm not admin. Chutíya sala.")

        return wrapper

    return decorator


# user you replied is a bot?
def if_bot():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            reply_msg = await event.get_reply_message()
            reply_msg.sender
            if not reply_msg.sender.bot:
                await func(event)
            else:
                await event.edit("That's a Bot I Guess. Please reply to actual users..")

        return wrapper

    return decorator


# set the pm limit
def pm_limit():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                await func(event)
            else:
                await event.edit(
                    "This Command Only Works In Groups. Try again in a group.."
                )

        return wrapper

    return decorator


# checks for groups
def no_grp():
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(event):
            if event.is_group:
                pass
            else:
                await func(event)

        return wrapper

    return decorator


# hellbot
