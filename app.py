from flask import Flask, send_from_directory
import os

# Resolve the directory that contains this script so file lookups work
# regardless of the working directory Gunicorn is launched from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_folder=BASE_DIR, static_url_path='')


@app.route('/')
def index():
    html_file = os.path.join(BASE_DIR, 'FINAL_DISSERTATION_REPORT.html')
    if os.path.exists(html_file):
        return send_from_directory(BASE_DIR, 'FINAL_DISSERTATION_REPORT.html')
    # Fallback: friendly landing page so the app always responds
    return (
        '<!DOCTYPE html><html><head><meta charset="UTF-8">'
        '<title>RMD</title></head><body>'
        '<h1>Welcome to RMD</h1>'
        '<p><a href="/dashboard">Go to Dashboard</a></p>'
        '</body></html>'
    ), 200, {'Content-Type': 'text/html; charset=utf-8'}


@app.route('/dashboard')
def dashboard():
    html_file = os.path.join(BASE_DIR, 'Unified_Forensic_Dashboard.html')
    if os.path.exists(html_file):
        return send_from_directory(BASE_DIR, 'Unified_Forensic_Dashboard.html')
    # Fallback: friendly response so the route never returns a hard 404
    return (
        '<!DOCTYPE html><html><head><meta charset="UTF-8">'
        '<title>Dashboard</title></head><body>'
        '<h1>Forensic Dashboard</h1>'
        '<p>Dashboard file not found. Please check the deployment.</p>'
        '<p><a href="/">Back to Home</a></p>'
        '</body></html>'
    ), 200, {'Content-Type': 'text/html; charset=utf-8'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

