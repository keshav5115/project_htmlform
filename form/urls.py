from django.urls import path
from form import views

app_name='form'

urlpatterns = [
    path('register/',views.registerview,name='register'),
    path('read/',views.readview,name='read'),
    path('record/<pk>/',views.getrecord,name='record'),
    path('update/<pk>/',views.updateview,name='update'),
    path('uprecord/',views.updaterecord,name='uprecord'),
    path('delete/',views.deleterecord,name='delete')
    
]