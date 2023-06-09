from rest_framework import routers
from .views import ModeloViewSet

router = routers.DefaultRouter()
router.register(r'', ModeloViewSet)

urlpatterns = router.urls
