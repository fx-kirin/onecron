import re

from setuptools import find_packages, setup

try:
    from pathlib import Path
except:
    from pathlib2 import Path


def read(filename):
    file_path = Path(__file__).parent / filename
    text_type = type(u"")
    with open(file_path, mode="r", encoding='utf-8') as f:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), f.read())


def get_requires():
    r_path = Path(__file__).parent / 'requirements.txt'
    if r_path.exists():
        with open(r_path) as f:
            required = f.read().splitlines()
    else:
        requred = []
    return required


setup(
    name="onecron",
    version="0.1.0",
    url="https://github.com/fx-kirin/onecron",
    license='MIT',

    author="fx-kirin",
    author_email="fx.kirin@gmail.com",

    description="sleep until next specified time.",
    long_description=read("README.rst"),

    scripts=["scripts/onecron", ],

    install_requires=get_requires(),

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    data_files=[('', ['requirements.txt'])],
)
