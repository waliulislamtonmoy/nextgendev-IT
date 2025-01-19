from django.urls import path

from App_Home.views import (
    HomeListView,
    HomeCreateView,
    HomeUpdateView,
    HomeDeleteView
)

urlpatterns = [
    path("homes/",HomeListView.as_view(),name="homes"),
    path("create-homes/",HomeCreateView.as_view(),name="create-homes"),
    path("update-homes/<int:pk>/",HomeUpdateView.as_view(),name="update-homes"),
     path("delete-homes/<int:pk>/",HomeDeleteView.as_view(),name="delete-homes"),
]
