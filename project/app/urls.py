from django.urls import path
from app.views import *


urlpatterns = [
    path('', register_page, name='register'),
    path('login/', login_page, name='login_page'),
    path('home/', home_page, name='home_page'),
    path('logout/', logout_view, name='logout_view'),]