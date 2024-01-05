from flask import Flask , render_template , request
import requests

app = Flask (__name__)

@app.route('/')
def homepage() :
    return render_template("index.html")

@app.route("/weatherapp", methods = ['POST', 'GET'])
def get_weatherdata() :
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'q' : request.form.get('city'), 'appid' : request.form.get('app.id'), 'units' : request.form.get('unit')}
    response = requests.get(url, params)
    data = response.json()
    return f"{data}"

if __name__ == '__main__' :
    app.run (host = "0.0.0.0", port = 5002)