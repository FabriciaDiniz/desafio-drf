from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'', ConsultaViewSet, 'consulta-list')

urlpatterns = router.urls
