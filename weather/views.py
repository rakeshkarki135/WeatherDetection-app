from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def home(request):
     if request.method=="POST":
          city=request.POST.get('city')
          res=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=167b42cca7e772793cc1c6390b746f0d').read()
          json_data=json.loads(res)
          data={
               'country_code':str(json_data['sys']['country']),
               'coordinate':str(json_data['coord']['lon']) + ' '+
               str(json_data['coord']['lat']),
               'temp':str(json_data['main']['temp'])+'k',
               'pressure':str(json_data['main']['pressure']),
               'humidity':str(json_data['main']['humidity']),
               'city':city,
          }
          
     else:
          data={}
          city=''
          
     return render(request,'index.html',data)
