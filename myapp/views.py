from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

# Create your views here.

def scrape(request):
    if request.method == "POST":
        siteName = request.POST["site"]
        page = requests.get(siteName)
        soup = BeautifulSoup(page.text, 'html.parser')

        # link_address = []

        for link in soup.find_all('a'):
            # link_address.append(link.get('href'))
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
    return render(request, 'myapp/result.html', {
        'data': data
    })

def clear(request):
    Link.objects.all().delete()
    return render(request, 'myapp/result.html')
