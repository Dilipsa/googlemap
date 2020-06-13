from django.urls import path
from .views import (
	location_view,
	location_display_view,
	)

app_name="googleapp"
urlpatterns = [
    path('', location_view, name="googleapp"),
    path('display/', location_display_view, name="googleapp_display"),
]
