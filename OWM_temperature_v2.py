#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    location = request.form['location']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+location+'&units=metric&APPID=227b324bc09ab8c6c89b5b3e47afb6cd')
#    json_object = r.text
#    return json_object
    json_object = r.json()
    description = str(json_object['weather'][0]['description'])
    temp = float(json_object['main']['temp'])
    wind = float(json_object['wind']['speed'])
    humidity = float(json_object['main']['humidity'])
    return render_template('temperature.html', temp=temp, location=location, description=description, wind=wind, humidity=humidity)

@app.route('/')
def index():
    return render_template('index.html')
    
    if self.allow_reuse_address:
     self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		
if __name__ == '__main__':
    app.debug = True
app.run(host='0.0.0.0', port=5000)