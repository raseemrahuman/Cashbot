from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('indiagold', views.indiagold, name='indiagold'),
    path('paytmcash', views.paytmcash, name='paytmcash'),
    path('fileuploaded', views.fileuploaded, name='fileuploaded'),
    # path('contact', views.contact, name='contact')
    #------------crypto links-------------------------
    path('Crypto', views.Crypto, name='Crypto'),
    path('wallet', views.wallet, name='wallet'),
    path('Telegramlink', views.Telegramlink, name='Telegramlink'),
]
