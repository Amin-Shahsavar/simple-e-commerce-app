from django.urls import path
from authers import views


urlpatterns = [
    path("", views.auther_list, name="auther-list"),
    path("<int:id>/", views.auther_detail, name="auther-detail"),
]
