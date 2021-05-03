from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from conduit.api.auth.views import AuthenticationViewset
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name="auth"

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'users', AuthenticationViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('users/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls))
]