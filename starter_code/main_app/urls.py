from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    psth('logout/',auth_views.LogoutView.as_view().name='logout')
    
]