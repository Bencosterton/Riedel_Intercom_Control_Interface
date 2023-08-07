from flask import Flask, render_template, request, jsonify
import os
import requests
import socket
import xml.etree.ElementTree as ET
import schedule
import time
import threading

app = Flask(__name__, static_folder='static')


#############################################
############## Load web page  ###############
#############################################

@app.route('/')
def index():
    return render_template('index.html')

#############################################
########### Send Fader values  ##############
#############################################

@app.route('/fader_1_mute', methods=['POST', 'GET'])
def fader_1_mute():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXPmute.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/fader_1_-27', methods=['POST', 'GET'])
def fader_1_27():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP-27dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '

@app.route('/fader_1_-20', methods=['POST', 'GET'])
def fader_1_20():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP-20dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/fader_1_-12', methods=['POST', 'GET'])
def fader_1_12():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP-12dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/fader_1_-6', methods=['POST', 'GET'])
def fader_1_6():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP-6dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/fader_1_0', methods=['POST', 'GET'])
def fader_1_0():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP0dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/fader_1_+5', methods=['POST', 'GET'])
def fader_1_5():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP+5dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/fader_1_+13', methods=['POST', 'GET'])
def fader_1_13():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['DIR2_to_TBU8_SetXP+13dB.xml']    
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}   
    # Read the XML data from files and send the HTTP POST request to the server
    for xml_file in xml_files:
        # Construct the absolute path of the XML file
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        # Read the XML data from file
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        # Send the HTTP POST request to the server
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
        
#############################################
########## Update Fader Value  ##############
#############################################


@app.route('/get_crosspoint_statuses', methods=['POST', 'GET'])
def get_crosspoint_statuses():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Set the server address and port number
    server_address = 'http://10.9.82.100:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}
    # Define the XML files to send for checking crosspoint statuses
    xml_files = {
        'DIR2_to_TBU8_GetXPStatus.xml': 'DIR2>TBU8',
    }

    # Initialize the crosspoint statuses dictionary
    crosspoint_statuses = {}

    # Send a request to each XML file and store the status in the dictionary
    for xml_file, key in xml_files.items():
        # Construct the absolute path of the XML file
        xml_path = os.path.join(script_dir, 'xml', xml_file)

        # Read the XML data from file
        with open(xml_path, 'r') as f:
            xml_data = f.read()

        try:
            # Send the HTTP POST request to the server
            response = requests.post(server_address, data=xml_data, headers=headers)
            response.raise_for_status()  # Raise an exception if status code is 4xx or 5xx

            # Get the response text and process it
            response_text = response.text
            has_error, value = process_i4_value_response(response_text)  # No need to pass display_name anymore

            # Store the status in the crosspoint statuses dictionary
            crosspoint_statuses[key] = value  # We negate the has_error value as 'True' means the crosspoint is active

        except requests.exceptions.RequestException as e:
            # Handle the exception by setting the status to False
            crosspoint_statuses[key] = False

    return jsonify(crosspoint_statuses)

##############################
# Checking response messages #
##############################

def process_i4_value_response(response):
    root = ET.fromstring(response)
    i4_values = []

    # Find all 'i4' elements within the 'data' element
    for value in root.findall('./params/param/value/array/data/value/i4'):
        i4_values.append(int(value.text))

    if len(i4_values) >= 2:
        # Return the second 'i4' value
        return (True, i4_values[1])
    else:
        return (False, "No i4 value found")



      
      
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True,port=5099)

