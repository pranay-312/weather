from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city=request.POST['city']

        source=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=78d37f1b1afaf3da7ae2659674d429a1').read()
        
        list_data=json.loads(source)

        data={
            "country_code":str(list_data['sys']['country']),
            "coordinate":str(list_data['coord']['lon'])+str(list_data['coord']['lat']),
            "temp":str(list_data['main']['temp'])+'k',
            "pressure":str(list_data['main']['pressure']),
            "humidity":str(list_data['main']['humidity']),
        }
        print(data)
    else:
        data={}
    return render(request,"index.html",data)    
