from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.SearchResultsView.as_view(), name='search_result'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdate.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('', views.PostList.as_view(), name='home'),
]