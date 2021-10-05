import random

__version__ = "2.0.0"
__author__ = "Pie Thrower"


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


def add_prefix(input, prefixes=PREFIXES):
    pre_type = type(prefixes)
    if type(input) != str:
        raise TypeError("Input must be a string")
    if pre_type not in (list, tuple):
        raise TypeError("Prefixes must be passed as a list or tuple")
    return random.choice(prefixes) + input


def add_suffix(input, suffixes=SUFFIXES):
    suf_type = type(suffixes)
    if type(input) != str:
        raise TypeError("Input must be a string")
    if suf_type not in (list, tuple):
        raise TypeError("Suffixes must be passed as a list or tuple")
    return input + random.choice(suffixes)


def add_affixes(input, prefixes=PREFIXES, suffixes=SUFFIXES):
    pre_type = type(prefixes)
    suf_type = type(suffixes)
    if type(input) != str:
        raise TypeError("Input must be a string")
    if pre_type not in (list, tuple):
        raise TypeError("Prefixes must be passed as a list or tuple")
    if suf_type not in (list, tuple):
        raise TypeError("Suffixes must be passed as a list or tuple")
    return random.choice(prefixes) + input + random.choice(suffixes)


def substitute(input, substitutions=SUBSTITUTIONS):
    sub_type = type(substitutions)
    if type(input) != str:
        raise TypeError("Input must be a string")
    if sub_type != dict:
        raise TypeError("Suffixes must be passed as a dictionary")
    for sub in substitutions:
        input = input.replace(sub, substitutions[sub])
    return input


def owo(input, substitutions=SUBSTITUTIONS, prefixes=PREFIXES, suffixes=SUFFIXES):
    pre_type = type(prefixes)
    suf_type = type(suffixes)
    sub_type = type(substitutions)
    if type(input) != str:
        raise TypeError("Input must be a string")
    if pre_type not in (list, tuple):
        raise TypeError("Prefixes must be passed as a list or tuple")
    if suf_type not in (list, tuple):
        raise TypeError("Suffixes must be passed as a list or tuple")
    if sub_type != dict:
        raise TypeError("Suffixes must be passed as a dictionary")
    return add_affixes(substitute(input, substitutions=substitutions), prefixes=prefixes, suffixes=suffixes)
