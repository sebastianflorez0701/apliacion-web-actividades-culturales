from rest_framework import routers
from .api import ProjectViewSetActividades, ProjectViewSetComentarios

router = routers.DefaultRouter()

router.register("actividades", ProjectViewSetActividades, "actividades")
router.register("comentarios", ProjectViewSetComentarios, "comentarios")

urlpatterns = router.urls
