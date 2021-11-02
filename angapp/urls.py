from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import generics, routers

router = routers.DefaultRouter()
router.register('projects', views.Project_objects)
router.register('profile', views.Profile_objects)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    # path('api/project/',views.Project_objects.as_view()),
    # path('api/profile/',views.Profile_objects.as_view()),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('projects/<str:post>', views.project, name='project'),
    path('search/', views.search_project, name='search'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)