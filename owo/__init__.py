'''owofies text'''

import random

__version__ = "2.0.2"
__author__ = "Pie Thrower"


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
    " ( ˘ ³˘)♥",
    " ( ͡° ᴥ ͡°)",
    " (´・ω・｀)",
    " (ʘᗩʘ\')",
    " (இωஇ )",
    " (๑•́ ₃ •̀๑)",
    " (• o •)",
    " (⁎˃ᆺ˂)",
    " (╯﹏╰）",
    " (●´ω｀●)",
    " (◠‿◠✿)",
    " (✿ ♡‿♡)",
    " (❁´◡`❁)",
    " (　\'◟ \')",
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
    " :O",
    " <{^v^}>",
    " >_<",
    " >_>",
    " UwU",
    " XDDD",
    " \\°○°/",
    " ^-^",
    " ^_^",
    " x3",
    " xD",
    " ÙωÙ",
    " ʕʘ‿ʘʔ",
    " ʕ•ᴥ•ʔ",
    " ミ(．．)ミ",
    " ㅇㅅㅇ",
    ", fwendo",
    "（＾ｖ＾）",
    " (　\"◟ \")",
    " *nuzzles u*",
    " x3c",
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


def add_prefix(input_string, prefixes=PREFIXES):
    '''Appends a random prefix to the beginning of the string'''
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    if not isinstance(prefixes, (list, tuple)):
        raise TypeError("Prefixes must be passed as a list or tuple")
    return random.choice(prefixes) + input_string


def add_suffix(input_string, suffixes=SUFFIXES):
    '''Appends a random suffix to the end of the string'''
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    if not isinstance(suffixes, (list, tuple)):
        raise TypeError("Suffixes must be passed as a list or tuple")
    return input_string + random.choice(suffixes)


def add_affixes(input_string, prefixes=PREFIXES, suffixes=SUFFIXES):
    '''Appends a random prefix and suffix to the beginning and end of the string'''
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    if not isinstance(prefixes, (list, tuple)):
        raise TypeError("Prefixes must be passed as a list or tuple")
    if not isinstance(suffixes, (list, tuple)):
        raise TypeError("Suffixes must be passed as a list or tuple")
    return random.choice(prefixes) + input_string + random.choice(suffixes)


def substitute(input_string, substitutions=None):
    '''owofies the string without adding affixes'''
    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string")
    if substitutions is None:
        substitutions = SUBSTITUTIONS
    if not isinstance(substitutions, dict):
        raise TypeError("Suffixes must be passed as a dictionary")
    for sub in substitutions:
        input_string = input_string.replace(sub, substitutions[sub])
    return input_string


def owo(input_string, substitutions=None, prefixes=PREFIXES, suffixes=SUFFIXES):
    '''owofies the string and adds a random prefix and suffix'''
    return add_affixes(substitute(input_string, substitutions=substitutions),
                       prefixes=prefixes, suffixes=suffixes)
