from django.urls import path
from .views.main_view import BlogView, category_view, product_view
from .views.auth_view import register_user, login_user
#from rest_framework_simplejwt.views import TokenRefreshView
# from .views import blog

urlpatterns = [
 path('blog/', BlogView.as_view()),
 path('register/', register_user),
 path('login/', login_user),
 path('product/', product_view),
 path('category/<int:id>/', category_view)
 #path('token/refresh', TokenRefreshView)
    # path('blog/', blog)
    
]