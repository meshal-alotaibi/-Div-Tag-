from django.urls import path
<<<<<<< HEAD
=======
from django.contrib.auth import views as auth_views
>>>>>>> 9f7a62ff02cb6321eae1e4eded43e5387cbf4b35
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
<<<<<<< HEAD
    psth('logout/',auth_views.LogoutView.as_view().name='logout')
    
]
=======
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    # template_name to opent loin file that in template folder #name -->is the url for login page
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('category/<int:category_id>/',
         views.category_topics, name='category_topics'),
    path('category/<int:category_id>/topics/<int:topic_id>/',
         views.topic, name='topic'),

]
>>>>>>> 9f7a62ff02cb6321eae1e4eded43e5387cbf4b35
