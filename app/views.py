from django.shortcuts import render

# Create your views here.

import datetime
datee=datetime.datetime.now()
def filters(request):
    return render(request,'filters.html',context={'data':'hai PYthon how are you','datee':datee,'count':1})