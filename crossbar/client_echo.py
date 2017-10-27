from __future__ import unicode_literals
from autobahn.twisted.component import Component, run

app = Component(transports='ws://127.0.0.1:8081/ws', realm='backend')


@app.subscribe('activity_stream')
def echo(*args, **kwargs):
    print('args {0}'.format(args))
    if kwargs:
        print('kwargs {0}'.format(kwargs))


if __name__ == '__main__':
    run(app)
