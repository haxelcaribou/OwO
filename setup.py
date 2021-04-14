from setuptools import setup

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README_md = f.read()

setup(
    name="text-to-owo",
    version="1.1.6",
    author="Pie Thrower",
    author_email="piethrowerchamp@gmail.com",
    python_requires=">=3",
    description="Translates normal text into OwO speak. Port from Zuzak's javascript version",
    long_description=README_md,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/piethrower/OwO",
    py_modules=["owo"],
    entry_points="""
        [console_scripts]
        owo = owo:owo
        substitute = owo:substitute
        add_affixes = owo:add_affixes
        add_prefix = owo:add_prefix
        add_suffix = owo:add_suffix
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Text Processing :: Filters",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ]
)
