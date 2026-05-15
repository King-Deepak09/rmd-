from flask import Flask
import os

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def index():
    html_file = 'FINAL_DISSERTATION_REPORT.html'
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            return f.read()
    return 'Welcome to RMD'


@app.route('/dashboard')
def dashboard():
    html_file = 'Unified_Forensic_Dashboard.html'
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            return f.read()
    return 'Dashboard not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
