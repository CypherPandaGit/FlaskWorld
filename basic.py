from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_list = [1, 2, 3, 4, 5]
    puppy_list = ['Fluffy', 'Rufus', 'Spike']
    user_logged_in = True

    return render_template('basic.html', my_list = my_list, puppy_list = puppy_list,
                           user_logged_in = user_logged_in)


if __name__ == '__main__':
    app.run(debug=True)
