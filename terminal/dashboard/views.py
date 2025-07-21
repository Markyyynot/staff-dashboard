from django.shortcuts import render, redirect
from .forms import TicketForm

def dashboard(request):
    if request.method == 'POST' and 'ticket_form_submit' in request.POST:
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('dashboard')  # reload to close modal
    else:
        ticket_form = TicketForm()

    return render(request, 'dashboard.html', {'ticket_form': ticket_form})

def driver_registration(request):
    return render(request, 'driver_registration.html')

def trip_schedule(request):
    return render(request, 'trip_schedule.html')
