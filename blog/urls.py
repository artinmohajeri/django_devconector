from django.urls import path
from .views import index_function, post_function, posts_function
urlpatterns = [
    path('',index_function ,name='index_function'),
    path('',posts_function ,name='posts_function'),
    path('',post_function ,name='post_function'),
]