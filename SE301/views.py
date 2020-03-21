from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


@login_required()
def admin_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "adminPage.html", {})


@login_required()
def doctor_view(request):
    return render(request, 'doctorPage.html', {'doctors': doctor_view()})


@login_required()
def doctor_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "doctorPage.html", {})


@login_required()
def patient_view(request, *args, **kwargs):
    return render(request, "patientPage.html", {'patients': patient_view()})


@login_required()
def patient_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "patientPage.html", {})


def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "contact.html", {})


def forget_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "accounts/forgetPassword.html", {})


def news_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "news.html", {})
