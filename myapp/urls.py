from django.urls import path
from . import views

urlpatterns = [
	path('index/',views.fn_index)
]