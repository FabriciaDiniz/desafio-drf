from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'', EspecialidadeViewSet, 'especialidade-list')

urlpatterns = router.urls
