#!/usr/bin/python3

import unittest

import owo

# assert(owo.add_prefix(str,prefixes=("test",)) == "test"+str)
# assert(owo.add_suffix(str,suffixes=("test",)) == str+"test")
# assert(owo.substitute(str,substitutions={"123":"abc"}) == "abc456789")
#
# owo.add_suffix(str,suffixes="test")
# owo.add_preffix(str,suffixes=("test",))


str = "123456789"
affix = ("abcdefg",)
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


class TestOwO(unittest.TestCase):

    def test_constants(self):
        self.assertIsInstance(owo.SUBSTITUTIONS, dict)
        self.assertIsInstance(owo.PREFIXES, tuple)
        self.assertIsInstance(owo.SUFFIXES, tuple)

    def test_substitution(self):
        for x in subs:
            self.assertEqual(owo.substitute(x), subs[x])
        with self.assertRaises(TypeError):
            owo.substitute(30)
        with self.assertRaises(TypeError):
            owo.substitute(str, substitutions=30)
        with self.assertRaises(TypeError):
            owo.substitute(str, substitutions="string")
        self.assertEqual(owo.substitute(
            str, substitutions={"123": "xyz"}), "xyz456789")

    def test_affixes(self):
        self.assertTrue(len(owo.add_affixes(str)) >= len(str))
        self.assertEqual(owo.add_affixes(str, prefixes=affix,
                         suffixes=affix), "abcdefg123456789abcdefg")
        with self.assertRaises(TypeError):
            owo.add_affixes(30)
        with self.assertRaises(TypeError):
            owo.add_affixes(str, prefixes=30)
        with self.assertRaises(TypeError):
            owo.add_affixes(str, prefixes="string")
        with self.assertRaises(TypeError):
            owo.add_affixes(str, suffixes=30)
        with self.assertRaises(TypeError):
            owo.add_affixes(str, suffixes="string")

    def test_prefixes(self):
        self.assertTrue(len(owo.add_prefix(str)) >= len(str))
        self.assertEqual(owo.add_prefix(
            str, prefixes=affix), "abcdefg123456789")
        with self.assertRaises(TypeError):
            owo.add_prefix(30)
        with self.assertRaises(TypeError):
            owo.add_prefix(str, prefixes=30)
        with self.assertRaises(TypeError):
            owo.add_prefix(str, prefixes="string")

    def test_suffixes(self):
        self.assertTrue(len(owo.add_suffix(str)) >= len(str))
        self.assertEqual(owo.add_suffix(
            str, suffixes=affix), "123456789abcdefg")
        with self.assertRaises(TypeError):
            owo.add_suffix(30)
        with self.assertRaises(TypeError):
            owo.add_suffix(str, suffixes=30)
        with self.assertRaises(TypeError):
            owo.add_suffix(str, suffixes="string")

    def test_owo(self):
        with self.assertRaises(TypeError):
            owo.owo(30)
        with self.assertRaises(TypeError):
            owo.owo(str, substitutions=30)
        with self.assertRaises(TypeError):
            owo.owo(str, substitutions="string")
        with self.assertRaises(TypeError):
            owo.owo(str, prefixes=30)
        with self.assertRaises(TypeError):
            owo.owo(str, prefixes="string")
        with self.assertRaises(TypeError):
            owo.owo(str, suffixes=30)
        with self.assertRaises(TypeError):
            owo.owo(str, suffixes="string")
        self.assertEqual(owo.owo(str, prefixes=affix, suffixes=affix, substitutions={
                         "123": "xyz"}), "abcdefgxyz456789abcdefg")


if __name__ == '__main__':
    # Main module
    unittest.main()
