from django.shortcuts import render
import requests


def index(request):
    text = request.GET.get('city', 'hyderabad')
    print(text)

    api_key = "27ca3b120a65f20327d620abdc6ccecd"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = text

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidity = y["humidity"]

        tempmin = y['temp_min']
        tempmax = y['temp_max']
        feel = y['feels_like']

        s = x['wind']
        ws = s['speed']
        wd = s['deg']

        v = x['visibility']

        z = x["weather"]

        weather_description = z[0]["description"]

        params = {'cit': text.upper(), 'curtemp': round(current_temperature - 273.15, 2), 'curpres': current_pressure,
                  'curhum': current_humidity, 'dec': weather_description.capitalize(),
                  'tmin': round(tempmin - 273.15, 2), 'tmax': round(tempmax - 273.15, 2),
                  'winds': ws, 'windd': wd, 'visb': round(v / 1000, 2), 'fee': round(feel - 273.15, 2)}
        return render(request, 'weather/index.html', params)

    else:
        print(" City Not Found ")

        params = {'cit': text.upper(), 'curtemp': '--', 'curpres': '--',
              'curhum': '--', 'dec': 'No information available', 'tmin': '--', 'tmax': '--',
              'winds': '--', 'windd': '--', 'visb': '--', 'fee': '--'}
        return render(request, 'weather/index.html', params)


def about(request):
    first = request.GET.get('firstname', 'default')
    last = request.GET.get('lastname', 'default')
    email = request.GET.get('inputEmail4', 'default')
    number = request.GET.get('contact', 'default')
    purpose = request.GET.get('purpose', 'default')
    addr = request.GET.get('inputAdress', 'default')
    city = request.GET.get('inputCity', 'default')
    state = request.GET.get('state', 'default')
    zip = request.GET.get('inputZip', 'default')

    print("get in touch")
    print("name:", first, last)
    print("email:", email)
    print("contact:", number)
    print("purpose:", purpose)
    print("address:", addr)
    print("city:", city, "state:", state)
    print("zip:", zip)

    return render(request, 'weather/about.html')


def contribute(request):
    return render(request, 'weather/contribute.html')


def complaint(request):
    first = request.GET.get('firstname', 'default')
    last = request.GET.get('lastname', 'default')
    email = request.GET.get('inputEmail4', 'default')
    number = request.GET.get('contact', 'default')
    city = request.GET.get('inputCity', 'default')
    state = request.GET.get('state', 'default')
    zip = request.GET.get('inputZip', 'default')
    complaint = request.GET.get('complaints', 'default')
    suggestion = request.GET.get('Suggestions', 'default')

    print("complaints/suggestion")
    print("name:", first, last)
    print("email:", email)
    print("contact:", number)
    print("complaints:", complaint)
    print("suggestions:", suggestion)
    print("city:", city, "state:", state)
    print("zip:", zip)

    return render(request, 'weather/complaint.html')
