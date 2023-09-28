from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.page1, name='registration'),
    path('login/',views.page2, name='login')
]
