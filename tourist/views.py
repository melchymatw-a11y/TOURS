from django.shortcuts import render

# Create your views here.
def buy_tickets(request):
    return render(request, 'buy_tickets.html')
def contacts(request):
    return render(request, 'contacts.html')
def index(request):
     return render(request, 'index.html')
def privacy(request):
     return render(request, 'privacy.html')
def speakerdetails(request):
     return render(request, 'speaker-details.html')
def starterpage(request):
     return render(request, 'starter-page.html')
def terms(request):
     return render(request, 'terms.html')
def venue(request):
    return render(request, 'venue.html')


