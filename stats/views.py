from django.shortcuts import render
from .corona import coronaData
# Create your views here.
data = coronaData()

def index(request):
	return render(request,"index.html", context={"data": data})