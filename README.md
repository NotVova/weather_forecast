# Weather Forecast

The project for study Django/API

# Local Developing

All actions should be executed from the source directory of the project and only after installing all requirements.


  1.Firstly, create and activate a new virtual environment:

    python3 -m venv ../venv
    source ../venv/bin/activate

  2.Install packages:

    pip install --upgrade pip
    pip install -r requirements.txt
    
  3.Enter your API key on 12 line in view.py. (https://openweathermap.org/)
  
    def weather_app(request):
      try:
          if request.method == 'POST':
              city = request.POST.get('city-forecast')

              params = {
                  'q': city,
                  'appid': ----> 'Your API KEY https://openweathermap.org/', <----
                  'units': 'metric'
              }

  4.Run project dependencies, migrations, fill the
  
    ./manage.py migrate
    ./manage.py runserver 
