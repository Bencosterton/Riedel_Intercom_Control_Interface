from flask import Flask, render_template, request
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_xml', methods=['POST'])
def process_xml():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML file
    xml_file = os.path.join(script_dir, 'xml', 'TX3_G1.xml')
    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'

    # Get the uploaded file from the HTML form
    uploaded_file = request.files['xml_file']
    
    # Read the XML data from the uploaded file
    xml_data = uploaded_file.read()

    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}

    # Send the HTTP POST request to the server
    response = requests.post(server_address, data=xml_data, headers=headers)

    # Process the response as necessary
    return render_template('results.html', response_text=response.text)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5193)
