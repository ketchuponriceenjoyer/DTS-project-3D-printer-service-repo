from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template('Home.html')

@app.route('/Session')
def render_Sessionpage():
    return render_template('Session.html')

@app.route('/images')
def render_imagespage():
    return render_template('images.html')

if __name__ == '__main__':
    app.run()