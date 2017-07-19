from flask import Flask, render_template, send_from_directory
import os
import paho.mqtt.client as mqtt

client= mqtt.Client()
client.connect("moorhouseassociates.com", 1883, 60)


app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html', to="Sarkodie Eric")

@app.route('/whereami')
def whereami():
    return 'kdua'


@app.route('/btn')
def btn():
        print ("button clicked")
	client.publish("test/all","Be vigilant")
        return ""

@app.route('/linux')
def linux():
      return render_template("linux.html")

@app.route("/python")
def python():
     return render_template("python.html")
