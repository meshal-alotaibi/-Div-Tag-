from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #url for authintication user and logIn , logOut , sginUp and changePassword
    path('signup', views.signup, name='signup'),
    # template_name to opent loin file that in template folder #name -->is the url for login page
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('setting/change_password', auth_views.PasswordChangeView.as_view(
        template_name='chang_pass.html'), name='change_password'),
    path('/change_password_successful',
         auth_views.PasswordChangeDoneView.as_view(template_name='PasswordChangeDone.html'), name='password_change_done'),
    path('account/',views.UserUpdateView.as_view(),name='my_account'),

    #url for the topics page 
    # url CRUD for topic
    path('category/<int:category_id>/new/',
         views.topicCreate.as_view(), name='create_topic'),
    path('category/<int:category_id>/topics/delete/<int:pk>',
         views.topicDelete.as_view(), name='delete_topic'),
    path('category/<int:category_id>/topics/edit/<int:pk>',
         views.topicUpdate.as_view(), name='update_topic'),

    # url for the topic page and CRUD for post
    path('category/<int:category_id>/topics/<int:topic_id>/',
         views.create_post, name='topic'),
    path('category/<int:category_id>/topics/<int:topic_id>/edit/<int:pk>/',
         views.postUpdate.as_view(), name='update_post'),
    path('category/<int:category_id>/topics/<int:topic_id>/delete/<int:pk>/',
         views.postDelete.as_view(), name='delete_post'),
     path('category/<int:category_id>/',
         views.category_topics, name='topics'),
     path('search',views.search,name='search' )    


      

    
]
