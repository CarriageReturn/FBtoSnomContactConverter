import os
import io
import urllib.request
import lxml.etree as ET

from flask import Flask, flash, request, redirect, render_template, Response

ALLOWED_EXTENSIONS = set(['xml'])

app = Flask(__name__)
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):

			flash('File successfully uploaded')

			data = file.read().decode('utf-8')

			data = data \
					.replace('<?xml version="1.0" encoding="utf-8"?>','') \
					.replace('<?xml version="1.0" encoding="UTF-8"?>','')
			
			dom = ET.fromstring(data)
			xslt = ET.parse('converter.xsl')

			transform = ET.XSLT(xslt)
			result = transform(dom)

			resultFile = io.StringIO(str(result))

			response = app.make_response(resultFile.read())
			response.headers.set('Content-Type', 'text/csv')
			response.headers.set('Content-Disposition', 'attachment', filename='output.csv')
			return response
		else:
			flash('Allowed file types are xml')
			return redirect(request.url)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')