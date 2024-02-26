from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('fruit/',views.fruits,name="fruit"),
    path('service/',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
    path('Login/Instagram/',views.login,name="login"),
]
