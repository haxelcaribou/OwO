import owo

subs = {
    "l": "w",
    "lllll": "wwwww",
    "r": "w",
    "rrrrr": "wwwww",
    "rlrlrl": "wwwwww",
    "notification": "nutification",
    "MPs reject Theresa May's revised EU withdrawal deal, throwing UK's Brexit plans into confusion":
    "MPs weject Thewesa May's wevised EU withdwawaw deaw, thwowing UK's Bwexit pwans into confusion"
}

for x in subs:
    print(owo.substitute(x) == subs[x])

str = "123456789"
print(len(owo.add_affixes(str)) >= len(str))

print(owo.add_prefix(str,prefixes=("test",)) == "test"+str)
print(owo.add_suffix(str,suffixes=("test",)) == str+"test")
print(owo.substitute(str,substitutions={"123":"abc"}) == "abc456789")
