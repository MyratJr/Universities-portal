from unicodedata import name
from django.urls import path
from .views import*
urlpatterns = [
    path('<str:dil>',index,name="index"),
    path('',home),
    path('teswir/<int:id>/<str:dil>',teswir,name='teswir'),
    path('beyan/<int:id>/<str:dil>',beyan,name='beyan'),
    path('news/<int:id>/<str:dil>',each_news,name='each_news'),
    path('all_news/<str:dil>',all_news,name='all_news'),
    path('yurt_uni/<str:dil>',yurt_uni,name='yurt_uni'),
    path('dil/<str:dil>/<str:page>',dil_,name='dil'),
    path('dil1/<str:dil>/<str:page>/<int:id>',dil_1,name='dil1'),
]