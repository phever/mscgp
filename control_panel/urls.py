from django.urls import path
from control_panel import views

urlpatterns = [
    path('', views.index_view, name='index')
]