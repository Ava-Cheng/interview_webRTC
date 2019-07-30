# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import uuid
import os
app = Flask(__name__)



@app.route('/')
def upload_file():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True ,port=3001, ssl_context=(
        "./rtc-video-room-cert.pem",
        "./rtc-video-room-key.pem"
    ))
