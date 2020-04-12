FROM python:3

RUN pip install flask lxml

ADD upload.py /
ADD converter.xsl /
ADD templates /templates

WORKDIR /

CMD [ "python", "upload.py" ]