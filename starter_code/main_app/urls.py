from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    # template_name to opent loin file that in template folder #name -->is the url for login page
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('category/<int:category_id>/',
         views.category_topics, name='category_topics'),
    path('category/<int:category_id>/topics/<int:topic_id>/',
         views.topic, name='topic '),
<<<<<<< HEAD
    path('category/<int:category_id>/new/',views.new_topic,name='new_topic')
=======
    path('category/<int:category_id>/new/',views.new_topic,name='new_topic '),
    path('setting/change_password',auth_views.PasswordChangeView.as_view(template_name='chang_pass.html'),name='change_password'),
    path('setting/change_password_successful',auth_views.PasswordChangeDoneView.as_view(template_name='pass_done.html'),name='pass_done')
>>>>>>> master


]
