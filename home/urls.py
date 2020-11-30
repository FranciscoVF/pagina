from django.urls import path
from django.contrib.auth import views as auth_views
from home import views

app_name = "paginas"

urlpatterns =[
    path('', views.Home.as_view(), name="home"),
]
