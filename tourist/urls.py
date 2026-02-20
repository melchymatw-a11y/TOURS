"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tourist import views

urlpatterns = {
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('venue/', views.venue, name='venue'),
    path('terms/', views.terms, name='terms'),
    path('starterpage/', views.starterpage, name='starter-pag'),
    path('speakerdetails/', views.speakerdetails, name='speaker-details'),
    path('privacy/', views.privacy, name='privacy'),
    path('contacts/', views.contacts, name='contacts'),
    path('buytickets/', views.buy_tickets, name='buy_tickets'),

}




