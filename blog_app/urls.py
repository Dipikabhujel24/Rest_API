from django.urls import path
from .views import BlogView
from .views.auth_view import register_user
# from .views import blog

urlpatterns = [
 path('blog/', BlogView.as_view()),
 path('register/', register_user)
    # path('blog/', blog)
    
]