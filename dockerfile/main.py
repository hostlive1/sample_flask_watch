from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route('/')
def digital_watch():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

