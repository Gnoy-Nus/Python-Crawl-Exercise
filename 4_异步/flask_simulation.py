import time

from flask import Flask

app =Flask(__name__)

@app.route('/sun')
def index_sun():
    time.sleep(2)
    return 'sun'


@app.route('/yong')
def index_yong():
    time.sleep(2)
    return 'yong'

if __name__ == '__main__':
    app.run()
