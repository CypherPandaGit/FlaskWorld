from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Welcome! Go to /puppy_latin/name to see your name in puppy latin!</h1>" \
           "<br>" \
           "<p>Let's do it</p>"

@app.route('/puppy_latin/<name>') # Fill this in!
def puppylatin(name):

    puppy_latin = ''

    if name[-1] == 'y':
        puppy_latin = name[0:-1] + 'iful'
    else:
        puppy_latin = name + 'y'

    return "Hi {}! Your puppylatin name is {}".format(name, puppy_latin)

if __name__ == '__main__':
    index()
