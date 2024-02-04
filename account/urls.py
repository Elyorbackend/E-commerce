from django.urls import path
from .views import RegisterView, homepage, LoginView, LogoutView, ProfileUpdate

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('home/',homepage,  name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('update/', ProfileUpdate.as_view(), name="update")
]