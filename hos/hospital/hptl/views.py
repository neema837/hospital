from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Department, Doctor,Booking


# Create your views here.
def doclist(request, d_slug=None):
    d_page = None
    doc = None
    if d_slug != None:
        d_page = get_object_or_404(Department, slug=d_slug)
        doc = Doctor.objects.filter(department=d_page)
    else:
        doc = Doctor.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            phonenum = request.POST['num']
            adr = request.POST['adr']
            email = request.POST['email']
            booking = Booking(name=name, email=email, address=adr,  num=phonenum, )
            booking.save()

    return render(request, 'index.html', {'dept': d_page, 'doc': doc})
