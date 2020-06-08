#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    return "probando"


if __name__ == "__main__": app.run()
