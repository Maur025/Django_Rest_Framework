from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() #Genera las rutas por defecto y las guarda en la variable

router.register('api/projects',ProjectViewSet,'projects')

urlpatterns = router.urls