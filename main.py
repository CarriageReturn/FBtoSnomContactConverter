import lxml.etree as ET

with open("converter.xml", 'r') as file:
    data = file.read() \
        .replace('<?xml version="1.0" encoding="utf-8"?>','') \
        .replace('<?xml version="1.0" encoding="UTF-8"?>','') \
        .replace('<telephonynid="1">','<telephonyn id="1">')

dom = ET.fromstring(data)
xslt = ET.parse('converter.xsl')

transform = ET.XSLT(xslt)
result = transform(dom)

text_file = open('output.csv', 'w')

text_file.write(str(result))
text_file.close()