import random

# TODO:
# Add blocklist for bad words
# Simpler way to handle uppercase ~ Use .title() and .upper()?

PREFIXES = (
    "<3 ",
    "0w0 ",
    "H-hewwo?? ",
    "HIIII! ",
    "Haiiii! ",
    "Huohhhh. ",
    "OWO ",
    "OwO ",
    "UwU ",
    "Whats this? "
)

SUFFIXES = (
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
    " *nuzzles u*",
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
    " x3c",
    " x3",
    " xD",
    " ÙωÙ",
    " ʕʘ‿ʘʔ",
    " ㅇㅅㅇ",
    ", fwendo",
    "（＾ｖ＾）",
    " nya~"
)

SUBSTITUTIONS = {
    "love": "wuv",  # keep before l->w
    "Love": "Wuv",
    "loving": "wuving",
    "Loving": "Wuving",
    "r": "w",
    "l": "w",
    "R": "W",
    "L": "W",
    # "ow": "OwO",
    "th ": "f ",
    "no": "nu",
    "No": "Nu",
    "has": "haz",
    "Has": "Haz",
    "have": "haz",
    "Have": "Haz",
    " says": " sez",
    " Says": " Sez",
    "you": "uu",
    "i've": "i",
    "I've": "I",
    "the ": "da ",
    "The ": "Da ",
    "qu": "qw",
    "Qu": "Qw",
    "pause ": "paws ",
    "Pause ": "Paws ",
    "paus": "paws",
    "Paus": "Paws"
}


def add_prefix(str, prefixes=PREFIXES):
    return random.choice(prefixes) + str


def add_suffix(str, suffixes=SUFFIXES):
    return str + random.choice(suffixes)


def add_affixes(str, prefixes=PREFIXES, suffixes=SUFFIXES):
    return random.choice(prefixes) + str + random.choice(suffixes)


def substitute(str, substitutions=SUBSTITUTIONS):
    for sub in substitutions:
        str = str.replace(sub, substitutions[sub])
    return str


def owo(str, substitutions=SUBSTITUTIONS, prefixes=PREFIXES, suffixes=SUFFIXES):
    return add_affixes(substitute(str, substitutions=substitutions), prefixes=prefixes, suffixes=suffixes)
