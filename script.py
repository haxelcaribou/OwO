#!/usr/bin/python3

import sys
import random

prefixes = (
    "<3 ",
    "0w0 ",
    "H-hewwo?? ",
    "HIIII! ",
    "Haiiii! ",
    "Huohhhh. ",
    "OWO ",
    "OwO ",
    "UwU "
)

suffixes = (
    " ( ͡° ᴥ ͡°)",
    " (இωஇ )",
    " (๑•́ ₃ •̀๑)",
    " (• o •)",
    " (●´ω｀●)",
    " (◠‿◠✿)",
    " (✿ ♡‿♡)",
    " (❁´◡`❁)",
    " (　\"◟ \")",
    " (人◕ω◕)",
    " (；ω；)",
    " (｀へ´)",
    " ._.",
    " :3",
    " :D",
    " :P",
    " ;-;",
    " ;3",
    " ;_;",
    " <{^v^}>",
    " >_<",
    " >_>",
    " UwU",
    " XDDD",
    " ^-^",
    " ^_^",
    " x3",
    " x3",
    " xD",
    " ÙωÙ",
    " ʕʘ‿ʘʔ",
    " ㅇㅅㅇ",
    ", fwendo",
    "（＾ｖ＾）"
)

substitutions = {
    "r": "w",
    "l": "w",
    "R": "W",
    "L": "W",
    # "ow": "OwO",
    "no": "nu",
    "has": "haz",
    "have": "haz",
    " says": " sez",
    "you": "uu",
    "I\"ve": "I",
    "the ": "da ",
    "The ": "Da ",
    "THE ": "THE "
}


def add_affixes(str):
    return random.choice(prefixes) + str + random.choice(suffixes)


def substitute(str):
    for sub in substitutions:
        str = str.replace(sub, substitutions[sub])
    return str


def owo(str):
    return add_affixes(substitute(str))


### Tests ###
# subs = {
#     "l": "w",
#     "lllll": "wwwww",
#     "r": "w",
#     "rrrrr": "wwwww",
#     "rlrlrl": "wwwwww",
#     "notification": "nutification",
#     "MPs reject Theresa May's revised EU withdrawal deal, throwing UK's Brexit plans into confusion":
#     "MPs weject Thewesa May's wevised EU withdwawaw deaw, thwowing UK's Bwexit pwans into confusion"
# }
#
# for x in subs:
#     print(substitute(x) == subs[x])
#
# str = "123456789"
# print(len(add_affixes(str)) >= len(str))
