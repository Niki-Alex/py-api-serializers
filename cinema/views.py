from rest_framework import viewsets

from cinema.models import Actor, Genre, Movie, MovieSession, CinemaHall
from cinema.serializers import (
    ActorSerializer,
    GenreSerializer,
    CinemaHallSerializer,
    MovieSerializer,
    MovieListSerializer,
    MovieDetailSerializer,
    MovieSessionSerializer,
    MovieSessionListSerializer,
    MovieSessionDetailSerializer,
)


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = (
        Movie.objects
        .all()
        .prefetch_related("genres")
        .prefetch_related("actors")
    )
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer

        if self.action == "retrieve":
            return MovieDetailSerializer

        return MovieSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = (
        MovieSession.objects
        .all()
        .select_related("movie")
        .select_related("cinema_hall")
    )
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer

        if self.action == "retrieve":
            return MovieSessionDetailSerializer

        return MovieSessionSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer
