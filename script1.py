import requests
from flask import Flask, render_template, request 

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET', 'POST'])
def index():

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST':
        city = request.form.get('city')

        if not city:
            return render_template('wrong.html')

    else:
        city = 'Las Vegas'
    
    try:
        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        return render_template('weather.html', weather=weather)
    except:
        return render_template('wrong.html')


app.run(debug=True)