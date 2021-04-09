# OwO

Yet another owoifier. This specific one is a port of @zuzak's JavaScript [OWO](https://github.com/zuzak/owo) into Python, because we needed this to be in even more languages.

# Install

1.  Run the command `pip install text-to-owo`.
2.  Add `import owo` to the beginning of your script.

# Usage

<code>add_prefix(*str*, *prefixes=DEFAULT*)</code>

Appends a random prefix to the beginning and end of the string.
Custom prefixes are optional and must be passed as an iterable.

<br/>

<code>add_suffix(*str*, *suffixes=DEFAULT*)</code>

Appends a random suffix to the beginning and end of the string.
Custom suffixes are optional and must be passed as an iterable.

<br/>

<code>add_affixes(*str*, *prefixes=DEFAULT*, *suffixes=DEFAULT*)</code>

Appends a random prefix and suffix to the beginning and end of the string.
Custom prefixes and suffixes are optional and must be passed as iterables.

<br/>

<code>substitute(*str*, *substitutions=DEFAULT*)</code>
Turns the text into owo speak without adding any prefixes or suffixes.
Custom substitutions are optional and must be passed as dictionary in the form `{"key":"replacement"}`.

<br/>

<code>owo(*str*, *prefixes=DEFAULT*, *suffixes=DEFAULT*, *substitutions=DEFAULT*)</code>

Both substitutes and adds prefixes and suffixes.
Optional prefixes, suffixes, and substitutions are the same as in other methods.

<br/>

For all optional arguments the given iterable/dict will replace the default values, not add to them.

If you pass in variables with the wrong data types I have no idea what will happen so don't do that.

# Example

```python
import owo

print(owo.owo("I have no mouth and I must scream"))
# HIIII! I haz nu mouth and I must scweam XDDD

print(owo.substitute("I have no mouth and I must scream"))
# I haz nu mouth and I must scweam
```
