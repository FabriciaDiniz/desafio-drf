from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r'', AgendaViewSet, 'consulta-list')

urlpatterns = router.urls
