from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
from flask_cors import CORS
#test
import time

#init socketio
socketio = SocketIO()

#Starting app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret!'
    socketio.init_app(app)

    CORS(app, )

    @app.route('/time')
    def get_time():
        current_time = { 'hour': 10, 'minute': 30 }
        return {'time': time.time()}
    return app



#Messages are received by both parties as events. 
# @socketio.on('message')
# def handle_message(data):
#     print('Received message: ' + data)

# # sending Messages
# @socketio.on('message')
# def handle_message(message):
#     send(message)



if __name__ == '__main__':
    app = create_app()
    socketio.run(app)