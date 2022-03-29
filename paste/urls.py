from django.urls import path
from paste import views

urlpatterns = [
    path('', views.PasteView.as_view(), name="paste"),
    path('/', views.PasteView.as_view(), name="paste"),
]