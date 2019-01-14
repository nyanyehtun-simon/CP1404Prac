from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello {}'.format(name)

@app.route('/f/<celsius_value>')
def f(celsius_value=0):
    return str(convert_celsius_to_fahrenheit(float(celsius_value)))

def convert_celsius_to_fahrenheit(celsius_value):
    #  returning fahrenheit value
    return celsius_value * 9.0 / 5 + 32

if __name__ == '__main__':
    app.run()
