import argparse
from flask import Flask, render_template, Response
from imageserve.stream import Image_Stream
import argparse

app = Flask(__name__)
source_dir = None
@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global source_dir
    global args
    return Response(gen(Image_Stream(source_dir, args.maxfr)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

parser = argparse.ArgumentParser('Image server')
parser.add_argument('sourcedir', help='Directory containing jpg files.')
parser.add_argument('--port', '-p', help='Port to serve stream on.', default=5000, type=int)
parser.add_argument('--maxfr', '-m', help='Maximum framerate in frames per second', type=int)
args = parser.parse_args()
source_dir = args.sourcedir
app.run(host='0.0.0.0', debug=False, port=args.port)