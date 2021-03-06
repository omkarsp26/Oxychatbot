# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:33:25 2022

@author: omkar
"""

import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

#from src.pythonREPL import execute_python, install_package

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').strip()
    isPythonCode = False
    resp = MessagingResponse()
    msg = resp.message()
    
    if incoming_msg.startswith('#!python3'):
        code = incoming_msg.lstrip('#!python3')
        output = execute_python(code)
        msg.body(output)
        isPythonCode = True
        
    elif incoming_msg.startswith('!pip install'):
        package = incoming_msg.split()[-1]
        output = install_package(package)
        msg.body(output)
        isPythonCode = True
        
    if isPythonCode:
        return str(resp)
# translator.translate("troubleshooting", dest="hi")   
    incoming_msg = incoming_msg.lower()
    
    if 'hi' in incoming_msg:
        #out=translator.translate("troubleshooting", dest='hi')
        output=(" This chatbot is in testing phase and is created by Omkar Patil for any doubts and concerns please contact me on 8329403968\n \nनमस्कार, ऑक्सीजन उपकरण एवं इससे संबंधित जानकारी के लिए आपका स्वागत है   \nजानकारी के लिए  विकल्प चुनें -  \n1 पीएसए समस्या निवारण और रखरखाव,  \n2 ऑक्सीजन सांद्रता समस्या निवारण और रखरखाव, \n3 एलएमओ टैंक एहतियाती उपाय, \n4 ऑक्सीजन सिलेंडर समस्या निवारण और रखरखाव \n5 PSA Oxygen Generator troubleshooting and maintenance details")
    
    elif '1' in incoming_msg:
        output = ("पीएसए संयंत्र - समस्या निवारण और रखरखाव के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें -  \n https://drive.google.com/file/d/1o3GC7rGjtjclPjyAe559AKnWG7jOTg-7/view?usp=sharing")
    
    elif '2' in incoming_msg:
        output = ("ऑक्सीजन सांद्रता यंत्र -  समस्या निवारण और रखरखाव के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें-  \n https://drive.google.com/file/d/10rTK94RVMw7z7ld9TJxUIaMIPKtEh2wi/view?usp=sharing")
    
    elif '3' in incoming_msg:
        output=("एलएमओ टैंक एहतियाती उपाय  के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें  -  https://drive.google.com/file/d/12P2jXN9PPpPMljEKWkRkAk55JZB9NjzS/view?usp=sharing") 
    
    elif '4' in incoming_msg:
        output=("ऑक्सीजन सिलेंडर समस्या निवारण और रखरखाव  के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें  - https://drive.google.com/file/d/1GnJbdDAGY8Qhey1I-luFBCjLVY1IcSFv/view?usp=sharing")
        
    elif '5' in incoming_msg:
        output=("PSA Troubleshooting\n \na compressor troubleshooting  \nb dryer troubleshooting \nc Adsorption tower troubleshooting")
        
    elif 'a' in incoming_msg:
        output=("If compressor is getting tripped in between then check the filters of the compressor  in case of blocked replace or clean the filters\n \n if compressor is failing to start then check the electrical connection of the compressor. In case of phase change or compressor starter relay related problem, Call the compressor OEM and reset the relay with the help of service engineer\n \n If compressor is showing overheating signal on HMI then check the ventilation of the PSA plant room, Even after proper ventilation if the compressor is showing overheating signal then connect with vendor and resgister a complaint")
    
    elif 'b' in incoming_msg:
        output=("if dryer is showing out of range dew point then contact service provider and rectify the issue with the help of vendor")
        
    elif 'c' in incoming_msg:
        output=("if adsorption tower is failing to purge nitrogen check the mufflers")
 
    msg.body(output)
    return str(resp) 

if __name__ == "__main__":
	app.run(debug=True)
        
    
