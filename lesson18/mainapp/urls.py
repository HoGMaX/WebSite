from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainpage,name = 'mainpage'),
    path('addcource',views.CreateCource.as_view(),name = 'add_cource'),
    path('allcource', views.SeeCourcePaige.as_view(), name='all_cource'),

]

