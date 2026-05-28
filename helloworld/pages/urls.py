# pages/urls.py
from django.urls import path  # import

# referring to views.py with from.views, thats how we get it here. home_page_view is part of that.
from .views import home_page_view

# There are two things going on here. The route is defined by empty string.
# Then a reference to the view home_page_view
urlpatterns = [path("", home_page_view)]
