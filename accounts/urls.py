from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/profile', views.UserProfileEdit.as_view(), name='user_profile'),
    path('<int:pk>/', views.user_index, name='user_index'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]