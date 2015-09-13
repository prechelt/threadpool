#!/usr/bin/env python

from setuptools import setup

# old: execfile('src/release.py')
# new:
with open('src/release.py') as f:
    code = compile(f.read(), 'src/release.py', 'exec')
    exec(code)

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    keywords=keywords,
    author=author,
    author_email=author_email,
    license=license,
    url=url,
    download_url=download_url,
    classifiers=classifiers,
    platforms=platforms,
    py_modules  = ['threadpool'],
    package_dir = {'': 'src'},
)
