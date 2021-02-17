from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    # template_name to opent loin file that in template folder #name -->is the url for login page
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login')

]
