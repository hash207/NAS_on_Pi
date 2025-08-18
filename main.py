from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
MEDIA_FOLDER = '/home/hashem-alsharif/Desktop/Hashem/My Work/NAS/media'

@app.route('/')
def index():
    files = os.listdir(MEDIA_FOLDER)
    media_files = [f for f in files if f.endswith(('.mp4', '.mp3'))]
    return render_template('index.html', media_files=media_files)

@app.route('/media/<filename>')
def stream_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
