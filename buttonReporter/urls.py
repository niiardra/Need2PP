from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('floor/<int:floor_id>/', views.floor, name='floor'),
    path('washroom/<int:washroom_id>/', views.washroom, name='washroom'),
]
