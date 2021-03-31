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


def add_prefix(str, prefixes=prefixes):
    return random.choice(prefixes) + str


def add_suffix(str, suffixes=suffixes):
    return str + random.choice(suffixes)


def add_affixes(str, prefixes=prefixes, suffixes=suffixes):
    return random.choice(prefixes) + str + random.choice(suffixes)


def substitute(str, substitutions=substitutions):
    for sub in substitutions:
        str = str.replace(sub, substitutions[sub])
    return str


def owo(str, substitutions=substitutions, prefixes=prefixes, suffixes=suffixes):
    return add_affixes(substitute(str, substitutions=substitutions), prefixes=prefixes, suffixes=suffixes)
