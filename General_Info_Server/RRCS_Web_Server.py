from flask import Flask, render_template, request
import os
import requests
import socket
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# This is the .xml file upload thing
@app.route('/process_xml', methods=['POST'])
def process_xml():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    server_address = 'http://127.0.0.1:8193'
    uploaded_file = request.files['xml_file']
    xml_data = uploaded_file.read()
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(server_address, data=xml_data, headers=headers)
    return render_template('results.html', response_text=response.text)

# This is the 'Get IFB List' Button
@app.route('/button001', methods=['POST', 'GET'])
def button001_clicked():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(script_dir, 'xml', 'GetIFBList.xml')
    server_address = 'http://127.0.0.1:8193'
    with open(xml_file, 'r') as f:
        xml_data = f.read()
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(server_address, data=xml_data, headers=headers)
    return render_template('results.html', response_text=response.text)

@app.route('/button002', methods=['POST', 'GET'])
def button002_clicked():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(script_dir, 'xml', 'GetLogicSource.xml')
    server_address = 'http://127.0.0.1:8193'
    with open(xml_file, 'r') as f:
        xml_data = f.read()
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(server_address, data=xml_data, headers=headers)
    return render_template('results.html', response_text=response.text)
    
@app.route('/button003', methods=['POST', 'GET'])
def button003_clicked():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(script_dir, 'xml', 'GetPort.xml')
    server_address = 'http://127.0.0.1:8193'
    with open(xml_file, 'r') as f:
        xml_data = f.read()
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(server_address, data=xml_data, headers=headers)
    return render_template('results.html', response_text=response.text)


@app.route('/button004', methods=['POST', 'GET'])
def button004_clicked():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(script_dir, 'xml', 'GetAllErrorCodes.xml')
    server_address = 'http://127.0.0.1:8193'
    with open(xml_file, 'r') as f:
        xml_data = f.read()
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(server_address, data=xml_data, headers=headers)
    return render_template('results.html', response_text=response.text)
    
@app.route('/button005', methods=['POST', 'GET'])
def button005_clicked():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_file = os.path.join(script_dir, 'xml', 'IsConnectedToArtist.xml')
    server_address = 'http://127.0.0.1:8193'
    with open(xml_file, 'r') as f:
        xml_data = f.read()
    headers = {'Content-Type': 'text/xml'}
    response = requests.post(server_address, data=xml_data, headers=headers)
    return render_template('results.html', response_text=response.text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5193)
