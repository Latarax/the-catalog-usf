from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import psycopg2
from .forms import RegisterForm

conn = psycopg2.connect( host="ec2-3-223-21-106.compute-1.amazonaws.com", user="fdnmfvethgnqkt", password="d8f82d08af92d50f7a117fb1537604bbbd2be24120847dce5910c0eed5eb52ad", dbname="d7hh193tgfderk" )

curruser = ''

def home(request):
    return render(request, 'catalog/index.html') 

def about(request):
    return render(request, 'catalog/about.html')

def mission(request):
    return render(request, 'catalog/mission.html')

def booklist(request):
    if request.method == 'POST':
        choice = request.POST['test']
        print(type(choice))
        choice = str(choice)
        print(choice)
        cur = conn.cursor()
        cur.execute("select * from library where title=%s", (choice, ))
        records = cur.fetchall()
        borrowed_username = curruser
        title = choice 
        original_username, author = '', ''
        print(f'Borrowed User is {borrowed_username}')

        for record in records:
            original_username = record[0]
            author = record[6]

        cur.execute("SELECT originalusername FROM checkedout WHERE originalusername=%s", (original_username, ))
        records = cur.fetchall()
        if(records):
            messages.warning(request, "Book already checked out")
            return redirect('catalog-booklist')
        else:
            cur.execute("INSERT INTO checkedout (borrowerusername, originalusername, title, author) VALUES (%s, %s, %s, %s)", (borrowed_username, original_username, title, author))
            conn.commit()        

            return redirect('catalog-registerSubmit')
    else:
        cur = conn.cursor()
        sample_query = "select * from library"
        cur.execute(sample_query)
        records = cur.fetchall()
    
        context = {'records':records}
    
        return render(request, 'catalog/booklist.html', context)

def checkout(request):
    return render(request, 'catalog/checkout.html')

def register(request):
    #form = UserCreationForm()
    if request.method == 'POST':
        print('yes')
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('user_name')
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            city = form.cleaned_data.get('city')
            password = form.cleaned_data.get('password')
            
            cur = conn.cursor()
            cur.execute("SELECT username FROM users WHERE username=%s", (username, ))
            records = cur.fetchall()
            if(records):
                messages.warning(request, "Username already in use")
                return redirect('catalog-register')
            else:
                print('no match')
                cur.execute("INSERT INTO users (username, password, firstname, lastname, city) VALUES (%s, %s, %s, %s, %s)", (username, password, firstname, lastname, city))
                conn.commit()
                context ={'username':username, 'password':password, 'firstname':firstname, 'lastname':lastname, 'city':city}

                global curruser
                curruser = username
                #print(curruser)

                return redirect('catalog-registerSubmit')
    else:
        #form = RegisterForm()
        print('yurp')
        context = {}
        context['form'] = RegisterForm()
    '''
    username = 'johndoe'
    password = '12345'
    firstname = 'john'
    lastname = 'doe'
    city = 'sayreville'
    
    '''
    return render(request, 'catalog/register.html', context)

def registerSubmit(request):
    print(curruser)
    print('working')
    cur = conn.cursor()
    cur.execute("SELECT * FROM checkedout WHERE borrowerusername=%s", (curruser, ))
    records = cur.fetchall()
    context = {'records':records}

    return render(request, 'catalog/test.html', context)