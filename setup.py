from setuptools import setup

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README_md = f.read()

setup(
    name="text-to-owo",
    version="1.1.0",
    author="Pie Thrower",
    author_email="piethrowerchamp@gmail.com",
    description="Translates normal text into OwO speak. Port from Zuzak's javascript version",
    long_description=README_md,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/piethrower/OwO",
    entry_points="""
        [console_scripts]
        owo = owo:owo
        c = owo:owo
        substitute = owo:substitute
        add_affixes = owo:add_affixes
        add_prefix = owo:add_prefix
        add_suffix = owo:add_suffix
    """
)
