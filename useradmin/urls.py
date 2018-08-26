from django.urls import path
from . import views

urlpatterns = [
    path('', views.userAdmin),
    path('<int:id>/', views.putUserAdmin),
]
