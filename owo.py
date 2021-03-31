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
