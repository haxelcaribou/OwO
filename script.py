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
#  "ow": "OwO",
  "no": "nu",
  "has": "haz",
  "have": "haz",
  " says": " sez",
  "you": "uu",
  "I\"ve" : "I",
  "the ": "da ",
  "The ": "Da ",
  "THE ": "THE "
}

def replace_all (string, key, replacement):
    if not (type(string) is string:
    	raise ValueError("Expected input to be a string, got"+type(string));

    if not(key and type(key) is string)


add_affixes = lambda str : random.choice(prefixes) + str + random.choice(suffixes)
substitute = lambda str : "not yet implemented" # TODO: actually do the thing
owo = lambda str : add_affixes(substitute(str))
