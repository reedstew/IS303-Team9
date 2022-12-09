from django.urls import path
from .views import indexPageView, victimsPageView, helpPageView
from .views import searchPageView, addPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("victims/", victimsPageView, name="victims"),
    path('search/', searchPageView, name="search"),
    path('add/', addPageView, name="add"),
    path("help", helpPageView, name="help")
]
