from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
urlpatterns = router.urls