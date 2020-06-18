from django.shortcuts import render
from .models import Offers, Gallery, BookedTable
# Create your views here.
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Offers
    templates = 'index.html'

#def home_view(request):
    # Get all blog posts
	#offer_date = Offers.objects.all().order_by('-pub_date')
    #offer_name = Offers.objects.all(pk=1)
	# Get all images
	#offer_img = Offers.objects.all()

	# Display all the posts
	#return render(request, 'index.html', {'offer_name':offer_name, 'offer_img': offer_img })


#def services_view(request):
    #return render(request, 'services.html')
class ServicesPageView(ListView):
    model = Gallery
    templates = 'services.html'


#def booking_view(request):
 #   form = {

  #  }
   # print(request.POST)
    #return render(request, 'table_book.html', {'form' : form})
class BookedTableCreateView(CreateView):
    model = BookedTable
    fields = ('name','email_id','mobile','tot_people','date','time')
    success_url = reverse_lazy('home')


def about_view(request):
    return render(request, 'about.html')
