from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('add-comment/<int:pk>/', views.AddComment.as_view(), name='add-comment'),
    path('massages/', views.MassagesView.as_view(), name='massages'),
    path('massage/<slug:slug>/', views.MassagesDetail.as_view(), name='massage-detail'),
]
