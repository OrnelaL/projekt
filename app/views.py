from django.shortcuts import render
from .models import *
# Mesazhi i konfirmimit ose jo te kontakti
from django.contrib import messages

# Create your views here.
def home(request):
    # shtojme paraqitjen e imazheve 
    # Te gjitha informacionet e modelit .obejcts metode
    # te gjitha ato wqe duam te shtojme do te jene ne je kotekst 
    # nqs perdorim metoden all te html do perdorim te html for in
    items = Item.objects.all()
    # Nga databaza te view
    # Nga view te html
    context = {"items":items}
    return render(request, "home.html", context)
    

def contact(request):
    if request.method == "POST":
        # Marrja e informacioneve nga inputet
        # name ehste vlera e atributit name
        # variabelCfareDo = request.POST['vlera e atributit name']
        firstNameInput = request.POST['name']
        lastNameInput = request.POST['lastName']
        emailInput = request.POST['email']
        commentInput = request.POST['comment']

    #   Kushtet nqs fushat jane boshe
        if firstNameInput != "" and lastNameInput != "" and emailInput != "" and commentInput != "":
            # Kalimi i seciles fushe e modelit Funx Contact nga modeli.py
            Contact(
                contact_name = firstNameInput,
                contact_surname = lastNameInput,
                contact_comment = commentInput,
                contact_email =  emailInput
                ).save()
            messages.success(request, "Message send.")
        else:
            messages.error(request, "Message not send")

            
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def detalis_item(request, id):
    # pk primary key. Marr informacione vetem per nje elemnt te caktuar
    # Behet dallimi ndermjet elementeve nga id (primary key)
    # Get nuk ka cikel
    itemInfos = Item.objects.get(pk=id)
    context = {"itemInfos": itemInfos}
    return render(request, "detalis_item.html", context)
