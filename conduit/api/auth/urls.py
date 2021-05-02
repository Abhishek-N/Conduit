from rest_framework.routers import SimpleRouter
from conduit.api.auth.views import AuthenticationViewset


app_name="auth"

# Create a router and register our viewsets with it.
router = SimpleRouter()
router.register(r'users', AuthenticationViewset)

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls