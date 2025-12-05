from django.urls import path, include
from .views import home, about, login_view, logout_view

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]