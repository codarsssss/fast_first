import pony
from pony.orm import *
import models

db = Database()


class User(db.Entity):
    user_id = Required(str)
    nick = Required(str)
    age = Required(int)
    wallets = Set('Wallet')


class Wallet(db.Entity):
    address = Required(str)
    private_key = Required(str)
    owner = Required(User)
