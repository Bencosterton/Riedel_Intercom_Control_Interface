from flask import Flask, render_template, request, jsonify
import os
import requests
import socket
import xml.etree.ElementTree as ET
import schedule
import time
import threading

app = Flask(__name__, static_folder='static')

@app.route('/', methods=['GET', 'POST'])
def index():
    # Fetch the crosspoint statuses from the audio router
    crosspoint_statuses = get_crosspoint_statuses()
    # Pass the crosspoint_statuses dictionary to the template
    return render_template('VORouting.html', crosspoint_statuses=crosspoint_statuses)

    return get_crosspoint_statuses()
    


#############################################
################ VO Routing  ################
#############################################

@app.route('/ACR1_VO1_on', methods=['POST', 'GET'])
def ACR1_VO1_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR1_to_VO1_SetXP.xml', 'VO1_to_ACR1_SetXP.xml' ,'VO1_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO1_G1.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR1_VO1_off', methods=['POST', 'GET'])
def ACR1_VO1_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO1_to_ACR1_KillXP.xml','ACR1_to_VO1_KillXP.xml', 'VO1_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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

@app.route('/ACR1_VO2_on', methods=['POST', 'GET'])
def ACR1_VO2_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR1_to_VO2_SetXP.xml', 'VO2_to_ACR1_SetXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = []    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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

@app.route('/ACR1_VO2_off', methods=['POST', 'GET'])
def ACR1_VO2_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO2_to_ACR1_KillXP.xml','ACR1_to_VO2_KillXP.xml',]    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR1_VO3_on', methods=['POST', 'GET'])
def ACR1_VO3_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR1_to_VO3_SetXP.xml', 'VO3_to_ACR1_SetXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = []    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR1_VO3_off', methods=['POST', 'GET'])
def ACR1_VO3_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO3_to_ACR1_KillXP.xml','ACR1_to_VO3_KillXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR1_VO4_on', methods=['POST', 'GET'])
def ACR1_VO4_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR1_to_VO4_SetXP.xml', 'VO4_to_ACR1_SetXP.xml' ,'VO4_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO4_G1.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR1_VO4_off', methods=['POST', 'GET'])
def ACR1_VO4_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO4_to_ACR1_KillXP.xml','ACR1_to_VO4_KillXP.xml', 'VO4_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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

@app.route('/ACR1_VO5_on', methods=['POST', 'GET'])
def ACR1_VO5_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR1_to_VO5_SetXP.xml', 'VO5_to_ACR1_SetXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = []    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR1_VO5_off', methods=['POST', 'GET'])
def ACR1_VO5_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO5_to_ACR1_KillXP.xml','ACR1_to_VO5_KillXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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



@app.route('/ACR2_VO1_on', methods=['POST', 'GET'])
def ACR2_VO1_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_to_VO1_SetXP.xml', 'VO1_to_ACR2_SetXP.xml', 'ACR2_VO_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_VO1.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR2_VO1_off', methods=['POST', 'GET'])
def ACR2_VO1_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO1_to_ACR2_KillXP.xml','ACR2_to_VO1_KillXP.xml', 'VO1_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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

@app.route('/ACR2_VO2_on', methods=['POST', 'GET'])
def ACR2_VO2_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_to_VO2_SetXP.xml', 'VO2_to_ACR2_SetXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = []    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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

@app.route('/ACR2_VO2_off', methods=['POST', 'GET'])
def ACR2_VO2_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO2_to_ACR2_KillXP.xml','ACR2_to_VO2_KillXP.xml',]    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR2_VO3_on', methods=['POST', 'GET'])
def ACR2_VO3_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_to_VO3_SetXP.xml', 'VO3_to_ACR2_SetXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = []    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR2_VO3_off', methods=['POST', 'GET'])
def ACR2_VO3_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO3_to_ACR2_KillXP.xml','ACR2_to_VO3_KillXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR2_VO4_on', methods=['POST', 'GET'])
def ACR2_VO4_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_to_VO4_SetXP.xml', 'VO4_to_ACR2_SetXP.xml', 'ACR2_VO_PARK.xml', 'VO4_PARK_Pres4.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_VO4.xml', 'VO4_G2_Pres4.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR2_VO4_off', methods=['POST', 'GET'])
def ACR2_VO4_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO4_to_ACR2_KillXP.xml','ACR2_to_VO4_KillXP.xml', 'VO4_PARK.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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

@app.route('/ACR2_VO5_on', methods=['POST', 'GET'])
def ACR2_VO5_on():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['ACR2_to_VO5_SetXP.xml', 'VO5_to_ACR2_SetXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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
    # reasign the panel

    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = []    
    # Set the server address and port numbers
    server_address = 'http://127.0.0.1:8193'
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
    
@app.route('/ACR2_VO5_off', methods=['POST', 'GET'])
def ACR2_VO5_off():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the absolute path of the XML files
    xml_files = ['VO5_to_ACR2_KillXP.xml','ACR2_to_VO5_KillXP.xml']    
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
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



    
########################################
## Checking the crosspoints in Artist ##
########################################

@app.route('/get_crosspoint_statuses', methods=['POST', 'GET'])

def get_crosspoint_statuses():
    # Get the absolute path of the directory containing this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Set the server address and port number
    server_address = 'http://127.0.0.1:8193'
    # Set the HTTP headers
    headers = {'Content-Type': 'text/xml'}
    # Define the XML files to send for checking crosspoint statuses
    xml_files = {
        'ACR1_VO1_GetXpStatus.xml': 'ACR1_VO1',
        'ACR1_VO2_GetXpStatus.xml': 'ACR1_VO2',
        'ACR1_VO3_GetXpStatus.xml': 'ACR1_VO3',
        'ACR1_VO4_GetXpStatus.xml': 'ACR1_VO4',
        'ACR1_VO5_GetXpStatus.xml': 'ACR1_VO5',
        'ACR2_VO1_GetXpStatus.xml': 'ACR2_VO1',
        'ACR2_VO2_GetXpStatus.xml': 'ACR2_VO2',
        'ACR2_VO3_GetXpStatus.xml': 'ACR2_VO3',
        'ACR2_VO4_GetXpStatus.xml': 'ACR2_VO4',
        'ACR2_VO5_GetXpStatus.xml': 'ACR2_VO5',
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
            has_error, message = process_boolean_response(response_text)  # No need to pass display_name anymore

            # Store the status in the crosspoint statuses dictionary
            crosspoint_statuses[key] = not has_error  # We negate the has_error value as 'True' means the crosspoint is active

        except requests.exceptions.RequestException as e:
            # Handle the exception by setting the status to False
            crosspoint_statuses[key] = False

    return jsonify(crosspoint_statuses)

##############################
# Checking response messages #
##############################

def process_boolean_response(response):
    root = ET.fromstring(response)
    boolean_value = None

    for data in root.findall('./params/param/value/array/data'):
        for value in data.findall('value'):
            if value.find('boolean') is not None:
                boolean_value = value.find('boolean').text.strip() == "0"
                break
        if boolean_value is not None:
            break

    if boolean_value is None:
        return (False, "No boolean value found")
    elif boolean_value:
        return (True, "")
    else:
        return (False, "")




if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5010)