from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/chat", methods=["GET"])
def show_template():
    return render_template("index.html")


@socketio.on("message")
def handle_message(data):
    print(f"client: {data}")
    msg = input("Eu: ")
    socketio.emit("message", f"server: {msg}")


@socketio.on("connect")
def handle_connect():
    print("Hosts connected")

if __name__ == "__main__":
    socketio.run(app, debug=True)