from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name='LogOX',
    version='1.0.0b1',
    author="Artem Eluzium",
    description=" My interlayer package for python logging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrEluzium/LogOX",
    license='Apache License 2.0',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: System :: Logging",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=find_packages(include=['LogOX', 'LogOX.*'])
)
