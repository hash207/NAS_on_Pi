from flask import Flask, render_template, send_from_directory, redirect, url_for
import os

app = Flask(__name__)
MEDIA_FOLDER = '/home/hashem-alsharif/Desktop/Hashem/My_Work/NAS_on_Pi/media'

def get_dir_contents(subpath=''):
    abs_path = os.path.join(MEDIA_FOLDER, subpath)
    items = []
    for entry in os.listdir(abs_path):
        entry_path = os.path.join(abs_path, entry)
        rel_path = os.path.join(subpath, entry) if subpath else entry
        if os.path.isdir(entry_path):
            items.append({'type': 'dir', 'name': entry, 'path': rel_path})
        elif entry.endswith('.mp4'):
            items.append({'type': 'video', 'name': entry, 'path': rel_path})
        else:
            items.append({'type': 'file', 'name': entry, 'path': rel_path})
    return items

@app.route('/')
def index():
    return redirect(url_for('browse', subpath=''))

@app.route('/browse/', defaults={'subpath': ''})
@app.route('/browse/<path:subpath>')
def browse(subpath):
    items = get_dir_contents(subpath)
    parent = os.path.dirname(subpath) if subpath else None
    # Pass through as before; template will include CSS
    return render_template('index.html', items=items, current_path=subpath, parent=parent)

@app.route('/media/<path:filename>')
def stream_file(filename):
    return send_from_directory(MEDIA_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
