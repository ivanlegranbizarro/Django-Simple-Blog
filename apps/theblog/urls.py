from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search-post/', views.SearchPostView.as_view(), name='post-search'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(),
         name='article-detail'),
    path('add-post/', views.AddPostView.as_view(), name='add-post'),
    path('update-post/<int:pk>', views.UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<int:pk>', views.DeletePostView.as_view(), name='delete-post'),
    path('category/<category_id>/', views.CatListView, name='category-post'),
    path('contact/', views.ContactView, name='contact'),
]
