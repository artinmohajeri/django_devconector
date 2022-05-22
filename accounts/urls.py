from django.urls import path
from .views import login_function, profile_function, register_function, add_education_function, add_experience_function, create_profile_function, dashboard_function,profiles_function

urlpatterns = [
    path('',login_function ,name='login_function'),
    path('',profile_function ,name='profile_function'),
    path('',register_function ,name='register_function'),
    path('',profiles_function ,name='profiles_function'),
    path('',add_education_function ,name='add_education_function'),
    path('',add_experience_function ,name='add_experience_function'),
    path('',create_profile_function ,name='create_profile_function'),
    path('',dashboard_function ,name='dashboard_function'),
]