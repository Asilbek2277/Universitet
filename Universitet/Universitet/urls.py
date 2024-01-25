from django.contrib import admin
from django.urls import path
from Ombor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fanlar/', fanlar),
    path('fanni_ochirish/<int:pk>/', fanni_ochirish),
    path('yonalish/', yonalish),
    path('y_ochir/<int:pk>/', y_ochir),
    path('ustozlar/', ustozlar),
    path('ustozni_ochirish/<int:pk>/', ustozni_ochirish),
]
