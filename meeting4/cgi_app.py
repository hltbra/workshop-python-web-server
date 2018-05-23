#!/Users/hugo/.virtualenvs/webserver-workshop/bin/python

import flask


app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.Response("Hello from Yipit!", status=404)


if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(app)
