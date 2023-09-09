from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persona', views.index),
    path('assets/images/logo-bec.png', views.asset_logo_file),
    path('favicon.ico', views.favicon),
    path('auth_cred_submit', views.auth_cred_submit),
    path('details', views.details),
    path('logout', views.logout_view),
]
