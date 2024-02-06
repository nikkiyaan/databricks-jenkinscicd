# Filename: setup.py
from setuptools import setup, find_packages

import dabdemo

setup(
  name = "dabdemo",
  version = dabdemo.__version__,
  author = dabdemo.__author__,
  url = "https://adb-3789614373587627.7.azuredatabricks.net/",
  author_email = "vrindarnair@gmail.com",
  description = "Python  Build",
  packages = find_packages(include = ["dabdemo"]),
  entry_points={"group_1": "run=dabdemo.__main__:main"},
  install_requires = ["setuptools"]
)
