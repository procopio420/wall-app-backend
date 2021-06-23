from django.urls import path

from . import views

urlpatterns = [
    path('wall/', views.MessageList.as_view(), name='wall_list'),
    path('wall/<int:pk>', views.MessageDetail.as_view(), name='wall_details'),
]
