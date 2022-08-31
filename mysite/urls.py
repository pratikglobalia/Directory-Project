from django.urls import path
from mysite import views

urlpatterns = [
    path('directory/', views.DirectoryView.as_view(), name='directory'),
    path('directory/<int:pk>/', views.DirectoryView.as_view(), name='directory'),
]