# -*- coding: UTF-8 -*-
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
import uuid


app = Flask(__name__)

@app.route('/audiovideo')
def upload_file():
    return render_template('index.html')

@app.route('/audiovideo', methods=['GET', 'POST'])
def audiovideo():
    if request.method == 'POST':
        file = request.files['audiovideo']
        uuidName = str(uuid.uuid1())
        filename_mkv = uuidName + ".mkv"
        filename = secure_filename(filename_mkv)
        file_save_path = os.path.join('.', 'static', 'uploads', filename_mkv)
        file.save(file_save_path)
    return "susses"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7881, debug=True, ssl_context=(
        "./rtc-video-room-cert.pem",
        "./rtc-video-room-key.pem"
    ))
