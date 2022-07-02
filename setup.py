# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2019/5/25 23:26

from setuptools import setup, find_packages

setup(
    name='re_helper',
    version='1.2.1',
    description=(
        're tool easy for use'
    ),
    keywords=(
        "re_helper"),
    long_description_content_type="text/markdown",
    long_description=open('README_PY.md', encoding='utf-8').read(),
    author='cc',
    author_email='abcdef123456chen@sohu.com',
    maintainer='cc',
    maintainer_email='abcdef123456chen@sohu.com',
    license='MIT License',
    install_requires=[
    ],
    url='https://github.com/abo123456789/re_helper',
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ])
