from sqlalchemy import Column, Numeric, String

from . import BASE, SESSION


class forceSubscribe(BASE):
    __tablename__ = "forceSubscribe"
    chat_id = Column(Numeric, primary_key=True)
    channel = Column(String)

    def __init__(self, chat_id, channel):
        self.chat_id = chat_id
        self.channel = channel


forceSubscribe.__table__.create(checkfirst=True)


def is_fsub(chat_id):
    try:
        return (
            SESSION.query(forceSubscribe)
            .filter(forceSubscribe.chat_id == chat_id)
            .one()
        )
    except:
        return None
    finally:
        SESSION.close()


def add_fsub(chat_id, channel):
    adder = SESSION.query(forceSubscribe).get(chat_id)
    if adder:
        adder.channel = channel
    else:
        adder = forceSubscribe(chat_id, channel)
    SESSION.add(adder)
    SESSION.commit()


def rm_fsub(chat_id):
    rem = SESSION.query(forceSubscribe).get(chat_id)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def all_fsub():
    rem = SESSION.query(forceSubscribe).all()
    SESSION.close()
    return rem
