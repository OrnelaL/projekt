from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homePage"),
    path("about/", views.about, name="aboutPage"),
    path("contact/", views.contact, name="contactPage"),
    path("service/", views.service, name="servicePage"),
    path("detalis_item/<id>/", views.detalis_item, name="detalisItemPage")
]