from django.shortcuts import render
from datetime import datetime
from ecomm.models import Contact, Book, Fibuy, Sell
from django.contrib import messages


def index(request):
    return render(request, 'ecomm/index.html')


# return HttpResponse('hhiiiiiiiiii')


def about(request):
    return render(request, 'ecomm/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'ecomm/contact.html')


def sell(request):
    if request.method == "POST":
        id = request.POST.get('id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        cate = request.POST.get('cate')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        money = request.POST.get('money')
        year = request.POST.get('year')
        a = Book.objects.get(id=id)
        sell = Sell(address=address, fname=fname, lname=lname, phone=phone, money=money, cate=cate, year=year,
                    prod_id=id)
        a.quant = a.quant - 1
        a.save()
        sell.save()
    return render(request, 'ecomm/sell.html')


def buy(request):
    bb = Book.objects.all()
    return render(request, 'ecomm/buy.html', {'bb': bb})


def jee(request):
    je = Book.objects.filter(cat='JEE')
    return render(request, 'ecomm/jee.html', {'je': je})


def cbse(request):
    cb = Book.objects.filter(cat='CBSE')
    return render(request, 'ecomm/cbse.html', {'cb': cb})


def state(request):
    st = Book.objects.filter(cat='STATE')
    return render(request, 'ecomm/state.html', {'st': st})


def engg(request):
    en = Book.objects.filter(cat='ENGG')
    return render(request, 'ecomm/engg.html', {'en': en})


def defence(request):
    de = Book.objects.filter(cat='DEFENCE')
    return render(request, 'ecomm/defence.html', {'de': de})


def icse(request):
    ic = Book.objects.filter(cat='ICSE')
    return render(request, 'ecomm/icse.html', {'ic': ic})


def fibuy(request, id):
    if request.method == "POST":
        id = request.POST.get('id')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        print(id)
        a = Book.objects.get(id=id)
        fibuy = Fibuy(address=address, email=email, phone=phone, prod_id=id)
        print(1)
        fibuy.save()
        a.quant = a.quant - 1
        a.save()
        return render(request, 'ecomm/good.html')

    if request.method == "GET":
        a = Book.objects.get(id=id)
        return render(request, 'ecomm/fibuy.html', {'a': a})


def final(request):
    return render(request, 'ecomm/good.html')


def good(request):
    # ic = Icse.objects.all()
    return render(request, 'ecomm/good.html')
