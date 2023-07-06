from . import views
from django.urls import path
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    path('game/', views.GameList.as_view(), name='game'),
    path('<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('', views.PlatformList.as_view(), name='home'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like')
]
