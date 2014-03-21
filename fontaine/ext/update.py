#!/usr/bin/env python
# coding: utf-8
# Only pyfontain developers should use this file to update files
import os
import os.path as op
import requests
import shutil


APPDATA_DIRNAME = 'pyfontaine'


def get_file(name, url):
    r = requests.get(url)
    if r.status_code == 200:
        with open(name, 'w') as f:
            f.write(r.content)
        return True


def get_from_cache(filename, url):
    try:
        #Windows code:
        directory = op.join(os.environ["APPDATA"], APPDATA_DIRNAME)
    except KeyError:
        #Linux and Mac code:
        directory = op.join(op.expanduser("~"), ".local", "share", APPDATA_DIRNAME)
    if not op.exists(directory):
        os.makedirs(directory)
    filepath = op.join(directory, filename)
    if not op.exists(filepath) and not get_file(filepath, url):
        shutil.copy(op.join(os.path.dirname(__file__), filename), filepath)
    return filepath


if __name__ == '__main__':
    get_file('Blocks.txt', 'http://www.unicode.org/Public/UNIDATA/Blocks.txt')
    get_file('languages.xml', 'https://raw.github.com/davelab6/extensis-languages/master/languages.xml')