import requests
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')
def search(request):
    search=request.POST['search']
    api = "c445762544df62f5dc5ccf510d289aea"

    list_of_data = requests.request("GET",
        'http://api.openweathermap.org/data/2.5/weather?q=' +search + '&units=metric&appid=' + api).json()

    # converting JSON data to a dictionary
    # list_of_data = json.loads(source)

    # data for variable list_of_data
    data = {
        # "country_code": str(list_of_data['sys']['country']),
        "cityname": str(list_of_data['name']),
        # "coordinate": str(list_of_data['coord']['lon']) + ' '
        # + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'C',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    return render(request, 'weather.html', data)