from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from identify.viewsets import ImagesPostViewSet
from users.viewsets import UserViewSet
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from rest_framework.documentation import include_docs_urls
# xadmin的url
import xadmin
from xadmin.plugins import xversion
xadmin.autodiscover()
# version模块自动注册需要版本控制的 Model
xversion.register_models()

router = DefaultRouter()
router.register('images', ImagesPostViewSet, 'images')
router.register('user', UserViewSet, 'users')


class RedirectToAPI(RedirectView):
    url = '/api/'


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/obtain/', obtain_jwt_token),
    path('api/', include(router.urls)),

    path('process/', RedirectToAPI.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('docs/', include_docs_urls(title='接口文档')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # 全局404页面配置
# handler404 = 'users.views.pag_not_found'
# # 全局500页面配置
# handler500 = 'users.views.page_error'
