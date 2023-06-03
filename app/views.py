from django.shortcuts import render
import requests


def weather_app(request):
    try:
        if request.method == 'POST':
            city = request.POST.get('city-forecast')

            params = {
                'q': city,
                'appid': 'Your API KEY https://openweathermap.org/',
                'units': 'metric'
            }
            response = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=params)
            data = response.json()
            weather_forecast = round(data['main']['temp'], 1)

            context = {
                'city': city,
                'title': 'Прогноз погоды',
                'weather_forecast': weather_forecast
            }
            return render(request=request, template_name='app/index.html', context=context)

        else:
            contex = {
                'title': 'Прогноз погоды'
            }
            return render(request=request, template_name='app/index.html', context=contex)
    except KeyError:
        context = {
            'title': 'Прогноз погоды',
            'error': 'Такого города нет!'
        }
        return render(request=request, template_name='app/index.html', context=context)
