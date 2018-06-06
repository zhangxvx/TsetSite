from django.conf.urls import include,url
from django.urls import path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)


app_name = 'quickstart'

# 使用自动化URL路由，转配我们的API.
# 如有额外需要, 我也为可视化API添加了登陆URLs.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]