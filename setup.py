import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ebook-translator',
    description='convert simplified chinese epub to traditional',
    version='1.0.0',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zachary Juang',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['ebook_converter'],
    install_requires=[
        'lxml',
        'ebooklib',
        'chinese-converter'
    ]
)
