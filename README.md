# OwO

Yet another owoifier. This specific one is a port of @zuzak's JavaScript [OWO](https://github.com/zuzak/owo) into Python, because we needed this to be in even more languages.

# Install

1.  Run the command `pip install text-to-owo` to install the package on your system.
2.  Add `import owo` to the beginning of your script.

# Usage

## Constants

<code>owo.**PREFIXES**</code>

Tuple containing default prefixes

<br/>

<code>owo.**SUFFIXES**</code>

Tuple containing default suffixes

<br/>

<code>owo.**SUBSTITUTIONS**</code>

Dict containing default substitutions


## Functions

<code>owo.**add_prefix**(*input*, *prefixes=owo.PREFIXES*)</code>

Appends a random prefix to the beginning and end of the string.
Custom prefixes are optional and must be passed as either a list or tuple of strings.

<br/>

<code>owo.**add_suffix**(*input*, *suffixes=owo.SUFFIXES*)</code>

Appends a random suffix to the beginning and end of the string.
Custom suffixes are optional and must be passed as either a list or tuple of strings.

<br/>

<code>owo.**add_affixes**(*input*, *prefixes=owo.PREFIXES*, *suffixes=owo.SUFFIXES*)</code>

Appends a random prefix and suffix to the beginning and end of the string.
Custom prefixes and suffixes are optional and must be passed as either a list or tuple of strings.

<br/>

<code>owo.**substitute**(*input*, *substitutions=owo.SUBSTITUTIONS*)</code>

Turns the text into owo speak without adding any prefixes or suffixes.
Custom substitutions are optional and must be passed as dictionary in the form `{"key":"replacement"}`.

<br/>

<code>owo.**owo**(*input*, *prefixes=owo.PREFIXES*, *suffixes=owo.SUFFIXES*, *substitutions=owo.SUBSTITUTIONS*)</code>

Both substitutes and adds prefixes and suffixes.
Optional prefixes, suffixes, and substitutions are the same as in other methods.

<br/>

For all optional arguments the given iterable/dict will replace the default values, not add to them.

All functions take a single string as input and output a string.


# Example

```python
import owo

print(owo.owo("I have no mouth and I must scream"))
# HIIII! I haz nu mouth and I must scweam XDDD

print(owo.substitute("I have no mouth and I must scream"))
# I haz nu mouth and I must scweam
```
