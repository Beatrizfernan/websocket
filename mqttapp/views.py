from django.shortcuts import render

def publish(request):
    return render(request, 'mqttapp/publish.html')

def subscribe(request):
    return render(request, 'mqttapp/subscribe.html')
