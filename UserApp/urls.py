from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.index),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('patient/', views.patient, name='patient'),
    path('doctor/', views.doctor, name='doctor'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
