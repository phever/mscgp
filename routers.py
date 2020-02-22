from rest_framework import routers
from api.views import MagicCardViewSet, MagicSetViewSet

router = routers.SimpleRouter()
router.register(r'sets', MagicSetViewSet)
router.register(r'cards', MagicCardViewSet)
router.register(r'', MagicCardViewSet)
urlpatterns = router.urls
