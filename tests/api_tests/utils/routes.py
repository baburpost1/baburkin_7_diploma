from enum import Enum


class ComboCards(str, Enum):
    LOGIN = 'login'
    CARDS = 'cards'
    MANAGE = 'manage'
    USERS = 'users'
    TRANSFER = 'bank_accounts/transfer'
    CONVERT = 'bank_accounts/convert'
