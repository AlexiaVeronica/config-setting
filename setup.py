from setuptools import setup, find_packages
import os
import requests


# 将markdown格式转换为rst格式
def md_to_rst(from_file, to_file):
    r = requests.post(url='http://c.docverter.com/convert',
                      data={'to': 'rst', 'from': 'markdown'},
                      files={'input_files[]': open(from_file, 'rb')})
    if r.ok:
        with open(to_file, "wb") as f:
            f.write(r.content)


md_to_rst("README.md", "README.rst")

if os.path.exists('README.rst'):
    long_description = open('README.rst', encoding="utf-8").read()
else:
    long_description = 'Add a fallback short description here'

if os.path.exists("requirements.txt"):
    install_requires = open("requirements.txt").read().split("\n")
else:
    install_requires = []

setup(
    name='config-setting',
    version='0.1',
    packages=find_packages(),
    package_data={"": ["*"]},  # 数据文件全部打包
    url='https://github.com/VeronicaAlexia/config-setting',
    license='MIT',
    author='Alexia',
    author_email='Elaina-Alex@proton.me',
    description='',
    include_package_data=True,  # 自动包含受版本控制(svn/git)的数据文件
    zip_safe=False,
)
