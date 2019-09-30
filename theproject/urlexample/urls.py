from django.urls import path
from . import views

urlpatterns = [
	path('profile/<int:username>/', views.profile),
	path('profile/<slug:article_value>/', views.article),
	path('profile/', views.profile)
]
