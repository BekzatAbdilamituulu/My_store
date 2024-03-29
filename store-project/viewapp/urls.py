from django.urls import path
from .views import index, about, contact, show_post, category_detail, search



urlpatterns = [
    path('', index, name = 'home'),
    path('about/', about, name='about'),
    path("search/", search, name="search"),
    path('contact/', contact, name='contact'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:cat_id>/', category_detail, name='category_detail'),
]

