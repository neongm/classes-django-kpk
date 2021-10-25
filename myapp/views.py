from django.shortcuts import render
from .models import Record

# Create your views here.

def index(req):
    records = Record.objects.order_by('record_title')
    context = {
        'records': records
    }
    return render(req, 'myapp/db_out.html', context)