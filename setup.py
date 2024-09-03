from setuptools import setup, find_packages

setup(
    name="pyinsight",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "textblob"
    ],
    author="Mehran Alam Beigi",
    author_email="mehraxxn@gmail.com",
    description="A Python library for interactive data analysis and visualization.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/mehranalam/pyinsight",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE",
        "Operating System :: OS Independent",
    ],
)
