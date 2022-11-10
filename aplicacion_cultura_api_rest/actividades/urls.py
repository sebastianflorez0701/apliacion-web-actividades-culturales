from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register("actividades", ProjectViewSet, "actividades")

urlpatterns = router.urls
