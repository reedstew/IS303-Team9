from django.urls import path
from .views import indexPageView, victimsPageView, helpPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("victims", victimsPageView, name="victims"),
    path("help", helpPageView, name="help")
]
