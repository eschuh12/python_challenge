import re


def parseText(textFile):
    d = {}
    with open(textFile) as file:
        txt = file.read()
        text = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', txt)
        d = dict(enumerate(text))

    return d
