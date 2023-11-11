from enum import Enum


class ComboCards(str, Enum):
    LOGIN = 'login'
    CARDS = 'cards'
    MANAGE = 'manage'
    USERS = 'users'
