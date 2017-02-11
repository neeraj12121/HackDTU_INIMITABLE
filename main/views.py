import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Input, Doctor, ImageProcessor

from .forms import InputForm


b = ImageProcessor()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")


def form(request):
    input_form = InputForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if input_form.is_valid():
            input_instance = input_form.save(commit = False)
            input_instance.save()
            return HttpResponseRedirect('/results/')
        else:
            form = InputForm()
    context = {
        "input_form" : input_form,
    }
    return render(request, "form.html", context)


def home(request):
    context = {}
    return render(request, "home.html", context)


def results(request):
    filename = Input.objects.latest("image").filename()
    print(filename)

    filename = MEDIA_ROOT + '/' + filename
    c = b.classify(filename)
    doctor_list = Doctor.objects.all().filter(tags=c)
    context = {
        "doctor_list" : doctor_list,
        "disease" : c
    }
    if c == "measles":
        messages.success(request, "You are diagnosed with " + c + ".")
        messages.success(request, "Medications: Fever reducers (such as acetaminophen (Tylenol, others), ibuprofen (Advil, Motrin, others) or naproxen (Aleve) to help relieve the fever that accompanies measles")
        messages.success(request, "Antibiotics")
        messages.success(request, "Vitamin A")
    if c == "rashes":
        messages.success(request, "You have " + c+ ".")
        messages.success(request, "Medications: Use gentle soaps such as Basis, Cetaphil, Dove, or Oil of Olay\n")
    if c == "chickenpox":
        messages.success(request, "You have " + c+ ".")
        messages.success(request, "Medications: Painkillers such as paracetamol")
        messages.success(request, "Antiviral medicine")
        messages.success(request, "Immunoglobin treatment")
        messages.success(request, "Wearing cool clothing would help too")
    if c == "pimples":
        messages.success(request, "Those are" + c+ ".")
        messages.success(request, "Medications: Benzonyl peroxide")
        messages.success(request,"Salicyclic acid")
        messages.success(request, "Azelaic acid, such as Azelex, a tropical cream")
        messages.success(request, "Androgen blockers, such as spinoronolactone")
    if c == "warts":
        messages.success(request, "Those are " + c+ ".")
        messages.success(request, "Medications: Strong peeling medicine")
        messages.success(request, "Freezing medicine" )
        messages.success(request, "Minor surgery Laser treatment")
    print(context["disease"])
    print(filename)


    return render(request, "results.html", context)

