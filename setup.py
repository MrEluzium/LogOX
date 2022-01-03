from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='LogOX',
    version='1.0.0',
    author="Artem Eluzium",
    description=" My interlayer package for python logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrEluzium/LogOX",
    packages=find_packages(include=['LogOX', 'LogOX.*'])
)
