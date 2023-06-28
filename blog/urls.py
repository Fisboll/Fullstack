from . import views
from django.urls import path
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('playstation/', views.Playstation.as_view(), name='playstation')
]
