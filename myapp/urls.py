from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from blog import views
from django.contrib import admin
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'post', views.PostViewSet)
router.register(r'post', views.PostViewSet, basename='Post')


urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
