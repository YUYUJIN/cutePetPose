import cv2
from flask import Flask, render_template, Response
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_data = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_data + b'\r\n')

@socketio.on('connect')
def test_connect():
    print('Client connected')
    for frame in generate_frames():
        socketio.emit('frame', {'data': frame})

@socketio.on('action')
def handle_action(json):
    action = json['action']
    # 행동을 처리하고, 해당 프레임을 캡쳐하는 코드를 작성합니다.


if __name__ == '__main__':
    socketio.run(app, debug=True) # 배포할땐 False 주의!!!
