from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import TripSchedule

def dashboard(request):
    if request.method == 'POST' and 'ticket_form_submit' in request.POST:
        ticket_form = TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('dashboard')  # reload to close modal
    else:
        ticket_form = TicketForm()

    trips = TripSchedule.objects.all().order_by('departure_time')  # ✅ add trips for the dashboard view

    return render(request, 'dashboard.html', {
        'ticket_form': ticket_form,
        'trips': trips,  # ✅ pass trips to template
    })

def driver_registration(request):
    return render(request, 'driver_registration.html')

def trip_schedule(request):
    trips = TripSchedule.objects.all().order_by('departure_time')
    return render(request, 'trip_schedule.html', {'trips': trips})
