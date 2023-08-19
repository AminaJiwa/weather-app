from django.shortcuts import render
from django.contrib import messages 
import requests
import datetime

# Create your views here.

def home(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'london'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3bd76958136524acd1cff83c6ed67bb0'
    PARAMS = {'units':'metric'}

    API_KEY = 'AIzaSyArO5e-r_rJleg6B9xcxxw2cOGI3KwE6P4'
    SEARCH_ENGINE_ID = '46568450ba0ee4654'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']

    try:
        data = requests.get(url,params=PARAMS).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, "index.html",{'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':city , 'exception_occurred':False ,'image_url':image_url})

    except KeyError:
        exception_occured = True
        messages.error(request, "Entered data is not available to API")
        day = datetime.day.today()
        return render(request, "index.html",{'description':description, 'icon':icon, 'temp':temp, 'day':day, 'city':'London' , 'exception_occurred':True})

