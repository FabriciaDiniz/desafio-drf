from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r'', AgendaViewSet, 'agenda-list')

urlpatterns = router.urls
