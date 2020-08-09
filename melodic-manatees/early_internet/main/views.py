import requests
from decouple import config
from django.shortcuts import render
from users.models import UserPreferences
import requests
from decouple import config


def main(request):

    news_key = config('NEWS_KEY')
    weather_key = config('WEATHER_KEY')
    
    news_url = 'https://api.nytimes.com/svc/topstories/v2/us.json?api-key=' + news_key
    nyt_usnews = requests.get(news_url).json()
    nyt_usnews_list = []

    for top_story in range(0, 4):
        nyt_usnews_list.append(
            {'title': nyt_usnews['results'][top_story]['title'],
             'abstract': nyt_usnews['results'][top_story]['abstract'],
             'url': nyt_usnews['results'][top_story]['url'],
             'img_small': nyt_usnews['results'][top_story]['multimedia'][0]['url']
             }
        )
        
    # THIS IS WHERE I AM HAVING PROBLEMS CALLING THE PREFERENCES!!!!!!!!!!!

    # city_name = getattr(UserPreferences, 'city_name')
    # country_name = getattr(UserPreferences, 'country_name')
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + \
          'london' + ',' + 'uk' + '&appid=' + weather_key + '&units=metric'
    # THESE CITIES SHOULD NOT BE HARDCODED

    city_weather = requests.get(weather_url).json()

    weather_dict = {'city': city_weather['name'],
                    'country': city_weather['sys']['country'],
                    'temperature': city_weather['main']['temp'],
                    'description': city_weather['weather'][0]['description']
                    }


    context = {
        'news': nyt_usnews_list,
        'weather': weather_dict,
    }

    if request.user.is_authenticated:
        context.update(
            {
                'pref': UserPreferences.objects.get(user=request.user)
            }
        )
        return render(request, 'main/dashboard.html', context)
    return render(request, 'main/dashboard.html', context)


def about(request):
    return render(request, 'main/main-about.html')
