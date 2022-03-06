# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:33:25 2022

@author: omkar
"""

import requests
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

#from src.pythonREPL import execute_python, install_package
import src.services as services

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
        output=(" This chatbot is in testing phase and is created by Omkar Patil for any doubts and concerns please contact me on 8329403968\n \nनमस्कार, ऑक्सीजन उपकरण एवं इससे संबंधित जानकारी के लिए आपका स्वागत है   \nजानकारी के लिए  विकल्प चुनें -  \n1 पीएसए समस्या निवारण और रखरखाव,  \n2 ऑक्सीजन सांद्रता समस्या निवारण और रखरखाव, \n3 एलएमओ टैंक एहतियाती उपाय, \n4 ऑक्सीजन सिलेंडर समस्या निवारण और रखरखाव")
    
    elif '1' in incoming_msg:
        output = ("पीएसए संयंत्र - समस्या निवारण और रखरखाव के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें -  \n https://drive.google.com/file/d/1o3GC7rGjtjclPjyAe559AKnWG7jOTg-7/view?usp=sharing")
    
    elif '2' in incoming_msg:
        output = ("ऑक्सीजन सांद्रता यंत्र -  समस्या निवारण और रखरखाव के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें-  \n https://drive.google.com/file/d/10rTK94RVMw7z7ld9TJxUIaMIPKtEh2wi/view?usp=sharing")
    
    elif '3' in incoming_msg:
        output=("एलएमओ टैंक एहतियाती उपाय  के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें  -  https://drive.google.com/file/d/12P2jXN9PPpPMljEKWkRkAk55JZB9NjzS/view?usp=sharing") 
    
    elif '4' in incoming_msg:
        output=("ऑक्सीजन सिलेंडर समस्या निवारण और रखरखाव  के बारे में अतिरिक्त जानकारी के लिए लिंक का अनुसरण करें  - https://drive.google.com/file/d/1GnJbdDAGY8Qhey1I-luFBCjLVY1IcSFv/view?usp=sharing")
   
    msg.body(output)
    return str(resp) 

if __name__ == "__main__":
	app.run(debug=True)
        
    
