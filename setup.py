from __future__ import annotations

from typing import List

from setuptools import find_packages, setup

classifiers: List[str] = [
    "Development status :: 5 - Production stable",
    "Intendent Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="crud",
    version="0.0.1",
    description="Conexion a mysql desde una aplicacion flask",
    url="",
    author="Alejandro Valenzuela Rivera",
    author_email="alejandrovalenzuela051@gmail.com",
    License="MIT",
    classifiers=classifiers,
    packages=find_packages(),
    install_requires=["Flask", "mariadb", "setuptools"],
)
