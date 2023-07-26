from django.shortcuts import render
import requests
import datetime

# Create your views here.

def home(request):
    appid = 'b6907d289e10d714a6e88b30761fae22'
    url = 'https://samples.openweathermap.org/data/2.5/forecast/hourly'
    params = {
        'q': 'London',
        'appid': appid,
        'units': 'metric'
    }
    
    r = requests.get(url= url, params=params)
    res = r.json()
    
    if 'list' in res and len(res['list']) > 0:
        forecast_data = res['list'][0]
        description = forecast_data['weather'][0]['description']
        icon = forecast_data['weather'][0]['icon']
        temp = forecast_data['main']['temp']
         
        day = datetime.date.today()
        
         
        return render(request, 'home.html', {'description': description, 'icon': icon, 'temp': temp, 'day': day})
    else:
        return render(request, 'home.html', {'error': 'Weather data not found'})
    



