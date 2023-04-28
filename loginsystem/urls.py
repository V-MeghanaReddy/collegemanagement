from django.urls import path

from loginsystem import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.loginfun,name='login'),
    path('register',views.registerfun,name='register'),
    path('readlogin',views.readlogin),
    path('readregister',views.register_read),
    path('logout',views.logoutfun,name='logout')

]