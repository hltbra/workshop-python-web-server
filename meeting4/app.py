#!/Users/hugo/.virtualenvs/webserver-workshop/bin/python

import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.Response("Hello from Python!", status=200)


@app.route("/p", methods=['POST'])
def p():
    return repr(dict(flask.request.form))


if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
