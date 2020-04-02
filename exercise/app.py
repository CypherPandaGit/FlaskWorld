from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/report')
def report():
    user_name = request.args.get('user_name')
    return render_template('report.html', user_name=user_name)

if __name__ == '__main__':
    app.run(debug=True)