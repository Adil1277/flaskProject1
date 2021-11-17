from flask import Flask, render_template, url_for

app = Flask(__name__)
@app.route('/')
@app.route('/home')
def main1():
    return render_template('doce.html')


@app.route('/about')
def about():
    return render_template('bodytemplate.html')

def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
