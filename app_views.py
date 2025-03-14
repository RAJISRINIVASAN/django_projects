from django.shortcuts import render
from .models import Datas

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')  # Use .get() to avoid KeyError
        age = request.POST.get('age', 0)
        address = request.POST.get('address', '')
        contact = request.POST.get('contact', 0)
        email = request.POST.get('email', '')

        # Create and save the object only for POST requests
        obj = Datas(name=name, age=age, address=address, contact=contact, email=email)
        obj.save()
        Mydata=Datas.objects.all()

        return render(request, 'home.html', {"message": "Registration Successful!"},{'datas':Mydata})

    return render(request, 'home.html')  # For GET requests










'''def product(request):
    mobile=int(request.GET["mobile"])
    keyboard=int(request.GET["keyboard"])
    monitor=int(request.GET["monitor"])
    price=mobile+keyboard+monitor
    return render(request,"result.html",{'price':price})'''
