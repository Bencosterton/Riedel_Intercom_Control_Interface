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
    crosspoint_statuses = get_crosspoint_statuses()
    return render_template('VORouting.html', crosspoint_statuses=crosspoint_statuses)
    return get_crosspoint_statuses()
    


#############################################
################ VO Routing  ################
#############################################

@app.route('/ACR1_VO1_on', methods=['POST', 'GET'])
def ACR1_VO1_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR1_to_VO1_SetXP.xml', 'VO1_to_ACR1_SetXP.xml' ,'VO1_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO1_G1.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR1_VO1_off', methods=['POST', 'GET'])
def ACR1_VO1_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO1_to_ACR1_KillXP.xml','ACR1_to_VO1_KillXP.xml', 'VO1_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '

@app.route('/ACR1_VO2_on', methods=['POST', 'GET'])
def ACR1_VO2_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR1_to_VO2_SetXP.xml', 'VO2_to_ACR1_SetXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = []    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '

@app.route('/ACR1_VO2_off', methods=['POST', 'GET'])
def ACR1_VO2_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO2_to_ACR1_KillXP.xml','ACR1_to_VO2_KillXP.xml',]    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '
    
@app.route('/ACR1_VO3_on', methods=['POST', 'GET'])
def ACR1_VO3_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR1_to_VO3_SetXP.xml', 'VO3_to_ACR1_SetXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = []    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR1_VO3_off', methods=['POST', 'GET'])
def ACR1_VO3_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO3_to_ACR1_KillXP.xml','ACR1_to_VO3_KillXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    return ' '
    
@app.route('/ACR1_VO4_on', methods=['POST', 'GET'])
def ACR1_VO4_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR1_to_VO4_SetXP.xml', 'VO4_to_ACR1_SetXP.xml' ,'VO4_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO4_G1.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR1_VO4_off', methods=['POST', 'GET'])
def ACR1_VO4_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO4_to_ACR1_KillXP.xml','ACR1_to_VO4_KillXP.xml', 'VO4_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)      
    return ' '

@app.route('/ACR1_VO5_on', methods=['POST', 'GET'])
def ACR1_VO5_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR1_to_VO5_SetXP.xml', 'VO5_to_ACR1_SetXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = []    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR1_VO5_off', methods=['POST', 'GET'])
def ACR1_VO5_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO5_to_ACR1_KillXP.xml','ACR1_to_VO5_KillXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '

@app.route('/ACR2_VO1_on', methods=['POST', 'GET'])
def ACR2_VO1_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_to_VO1_SetXP.xml', 'VO1_to_ACR2_SetXP.xml', 'ACR2_VO_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_VO1.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR2_VO1_off', methods=['POST', 'GET'])
def ACR2_VO1_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO1_to_ACR2_KillXP.xml','ACR2_to_VO1_KillXP.xml', 'VO1_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '

@app.route('/ACR2_VO2_on', methods=['POST', 'GET'])
def ACR2_VO2_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_to_VO2_SetXP.xml', 'VO2_to_ACR2_SetXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = []    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '

@app.route('/ACR2_VO2_off', methods=['POST', 'GET'])
def ACR2_VO2_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO2_to_ACR2_KillXP.xml','ACR2_to_VO2_KillXP.xml',]    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '
    
@app.route('/ACR2_VO3_on', methods=['POST', 'GET'])
def ACR2_VO3_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_to_VO3_SetXP.xml', 'VO3_to_ACR2_SetXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = []    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR2_VO3_off', methods=['POST', 'GET'])
def ACR2_VO3_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO3_to_ACR2_KillXP.xml','ACR2_to_VO3_KillXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '
    
@app.route('/ACR2_VO4_on', methods=['POST', 'GET'])
def ACR2_VO4_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_to_VO4_SetXP.xml', 'VO4_to_ACR2_SetXP.xml', 'ACR2_VO_PARK.xml', 'VO4_PARK_Pres4.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_VO4.xml', 'VO4_G2_Pres4.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR2_VO4_off', methods=['POST', 'GET'])
def ACR2_VO4_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO4_to_ACR2_KillXP.xml','ACR2_to_VO4_KillXP.xml', 'VO4_PARK.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)        
    return ' '

@app.route('/ACR2_VO5_on', methods=['POST', 'GET'])
def ACR2_VO5_on():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['ACR2_to_VO5_SetXP.xml', 'VO5_to_ACR2_SetXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
    # reasign the panel

    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = []    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)       
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)   
    return ' '
    
@app.route('/ACR2_VO5_off', methods=['POST', 'GET'])
def ACR2_VO5_off():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    xml_files = ['VO5_to_ACR2_KillXP.xml','ACR2_to_VO5_KillXP.xml']    
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}   
    for xml_file in xml_files:
        xml_file_path = os.path.join(script_dir, 'xml', xml_file)        
        with open(xml_file_path, 'r') as f:
            xml_data = f.read()           
        requests.post(server_address, data=xml_data, headers=headers)
        
    return ' '



    
########################################
## Checking the crosspoints in Artist ##
########################################

@app.route('/get_crosspoint_statuses', methods=['POST', 'GET'])

def get_crosspoint_statuses():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    server_address = 'http://127.0.0.1:8193'
    headers = {'Content-Type': 'text/xml'}
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

    crosspoint_statuses = {}

    for xml_file, key in xml_files.items():
        xml_path = os.path.join(script_dir, 'xml', xml_file)

        with open(xml_path, 'r') as f:
            xml_data = f.read()

        try:
            response = requests.post(server_address, data=xml_data, headers=headers)
            response.raise_for_status()

            response_text = response.text
            has_error, message = process_boolean_response(response_text) 


            crosspoint_statuses[key] = not has_error 

        except requests.exceptions.RequestException as e:
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
