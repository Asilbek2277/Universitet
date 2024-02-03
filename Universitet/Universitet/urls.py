from django.contrib import admin
from django.urls import path
from Ombor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fanlar/', fanlar),
    path('fanlar/<int:pk>/tahrirlash/', fanlarni_tahrirlash),
    path('fanni_ochirish/<int:pk>/', fanni_ochirish),
    path('yonalish/', yonalish),
    path('yonalishlar/<int:pk>/tahrirlash/', yonalish_tahrirlash),
    path('y_ochir/<int:pk>/', y_ochir),

    path('ustozlar/', ustozlar),
    path('ustozlar/<int:pk>/tahrirlash/', Ustozni_tahrirlash),

    path('ustozni_ochirish/<int:pk>/', ustozni_ochirish),
]
