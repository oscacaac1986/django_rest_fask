from rest_framework import routers

from project.api import ProjectViewSet

routers=routers.DefaultRouter()

routers.register('api/projects',ProjectViewSet,'projects')

urlpatterns=routers.urls