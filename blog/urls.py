from . import views
from django.urls import path
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('playstation/', views.Playstation.as_view(), name='playstation'),
    path('<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PlatformList.as_view(), name='home'),
]
