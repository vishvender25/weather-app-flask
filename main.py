import requests
from flask import Flask , render_template
from flask import request as flask_request

def find_weather_details(city_name):
    api_key = '31293255c56727a0052c4e85b57db30e'
    
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    
    response = requests.get(url=base_url)
    data = response.json()
    curr_temp_in_c = format(float(data['main']['temp']) - 273.15 , '0.2f')
    feels_like_in_c = format(float(data['main']['feels_like']) - 273.15 , '0.2f')
    
    return (curr_temp_in_c , feels_like_in_c)


app = Flask(__name__)
# bootstrap = Bootstrap5(app)

city_name = ''
@app.route('/' , methods= ['GET' , 'POST'])
def home():
   
    if flask_request.method == 'POST':
        city_name = flask_request.form['city']
        temperatures = find_weather_details(city_name)

        return render_template('weather.html' , city = city_name , curr_temp = temperatures[0] , feels_like = temperatures[1])
    return render_template('index.html')

@app.route('/weather' , methods = ['GET' , 'POST'])
def weather_details():
    return render_template('weather.html' , city = city_name)
    


if __name__ == '__main__':
    app.run(debug=True)





