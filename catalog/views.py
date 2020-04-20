from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

def home(request):
    return render(request, 'catalog/index.html') 

def about(request):
    return render(request, 'catalog/about.html')

def mission(request):
    return render(request, 'catalog/mission.html')

def booklist(request):
    conn = psycopg2.connect( host="ec2-3-223-21-106.compute-1.amazonaws.com", user="fdnmfvethgnqkt", password="d8f82d08af92d50f7a117fb1537604bbbd2be24120847dce5910c0eed5eb52ad", dbname="d7hh193tgfderk" )
    cur = conn.cursor()
    sample_query = "select * from library"
    cur.execute(sample_query)
    records = cur.fetchall()

    context = {'records':records}

    return render(request, 'catalog/booklist.html', context)

def checkout(request):
    return render(request, 'catalog/checkout.html')

def register(request):
    return render(request, 'catalog/register.html')