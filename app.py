from flask.app import Flask
from flask.templating import render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
io = SocketIO(app)

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/teste")
def teste():
    return render_template("teste.html")

@io.on('sendMessage')
def send_message_handler(msg):
    emit('getMessage', msg, broadcast=True )

if __name__ == '__main__':
    io.run(app, debug=True)