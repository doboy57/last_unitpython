from django.urls import path 

from. import views

app_name = 'Mainapp'

URLPattern =[
    path('',views.index,name='index')
]
