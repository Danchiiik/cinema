from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.films.views import FilmApiView, ReviewApiView

router = DefaultRouter()
router.register('review', ReviewApiView)
router.register('', FilmApiView)

urlpatterns = [
]
urlpatterns += router.urls