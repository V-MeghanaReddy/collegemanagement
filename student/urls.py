from django.urls import path

from student import views

urlpatterns = [
    path('',views.home),
    path('displaystudent',views.displaystudent,name='displaystudent'),
    path('addstudent',views.addstudent,name='addstudent'),
    path('readstudentdata',views.readstudentdata),
    path('update/<int:id>',views.updatedata,name='update'),
    path('delete/<int:id>',views.deletedata,name='delete'),
    path('logout', views.logoutfun, name='logout')

]


