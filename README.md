# OwO

This is a port of @zuzak's JavaScript [OWO](https://github.com/zuzak/owo) into Python, because we needed this to be in even more languages.

# Install

1.  Run the command `pip install owo`.
2.  Add `import owo` to the beginning of your script.

# Usage

The three available methods are `add_affixes`, `substitute`, and `owo`.

Each takes exactly one argument, which is the string to be owoified.

<br/>

`add_affixes` will append a random prefix and suffix to the beginning and end of the string.

`substitute` will turn the text into owo speak but not add any prefixes or suffixes.

`owo` will both add affixes and substitute.

# Example

```python
import owo

print(owo.owo("I have no mouth and I must scream"))
# HIIII! I haz nu mouth and I must scweam XDDD
```
