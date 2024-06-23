from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'variable': "am the one"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')



def testApi(request):
    try:
        if request.method == "GET":
            return JsonResponse({"message":"succes"},status=200)
        else:
            return JsonResponse({"message":"method not allowed"},status=405)
    except Exception as e:
        print(f"ERROR : {str(e)}")
        return JsonResponse({"message":str(e)},status=500)