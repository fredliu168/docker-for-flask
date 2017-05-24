# -*- coding: UTF-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    fo = open("foo.txt", "wb")
    fo.write(b"I'am run in docker!")
    fo.close()
    return 'Flask Dockerized fred hhaha'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')