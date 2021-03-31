from setuptools import setup

setup(
    name="text-to-owo",
    version="1.0.0",
    author="Pie Thrower",
    author_email="piethrowerchamp@gmail.com",
    description="Translates normal text into OwO speak. Port from Zuzak's javascript version",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/piethrower/OwO",
    entry_points="""
        [console_scripts]
        owo = owo:owo
        substitute = owo:substitute
        add_affixes = owo:add_affixes
    """
)
