# pages/urls.py
from django.urls import path  # import

from .views import home_page_view

urlpatterns = [path("", home_page_view)]
