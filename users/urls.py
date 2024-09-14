from django.urls import path

from .views import LoginView, Index

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('index/', Index.as_view(), name='index')
]
