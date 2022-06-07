from django.http import HttpResponseRedirect
from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import *
from .forms import VenueForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import MerchSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly


# Create your views here.
class MerchList(APIView):

    def get(self, request, format=None):
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = MerchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAdminOrReadOnly,)



def show_venues(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)

    return render(request,'events/show.html',{'venue':venue})





def list_venues(request): 

    venue_list= Venue.objects.all()

    return render(request,'events/venues.html',{'venue_list':venue_list})



def add_venue(request):

    submitted = False
    if request.method == 'POST':
          form = VenueForm(request.POST)
          if form.is_valid():
              form.save()
              return HttpResponseRedirect('/venue?submitted=True')
    else:
        form= VenueForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,'events/venue.html',{'form':form,'submitted':submitted})

def all_events(request):
    event_list= Event.objects.all()

    return render(request,'events/event.html',{
        'event_list':event_list,
    })


def home(request,year=datetime.now().year, month= datetime.now().strftime('%B')):

#convert to uppercase
    month= month.title() #capitalize() also works

#converting month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

#creating calendar
    cal = HTMLCalendar().formatmonth(
        year,
        month_number)

#Get a current year
    now = datetime.now()
    current_year = now.year

#Get the current TIME
    time = now.strftime('%I:%M:%S %p')


    return render(request,'events/home.html',{
        "year":year,
        "month": month,
        "month_number": month_number,
        "cal":cal,
        "current_year": current_year,
        "time": time,
    })