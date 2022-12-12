from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from applications.films.models import Films, Review
from applications.films.serializer import FilmSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter 



class FilmApiView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    
    
class ReviewApiView(mixins.ListModelMixin, mixins.CreateModelMixin ,GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    


