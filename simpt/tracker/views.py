from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.


class SectionList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SectionSerializer

    def get_queryset(self):
        user = self.request.user
        return Section.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user.id
        request.data['user'] = user
        return self.create(request, *args, **kwargs)


class SectionPK(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    serializer_class = SectionSerializer

    def get_queryset(self):
        user = self.request.user.id
        self.request.data['user'] = user
        return Section.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class StatusList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StatusSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Status.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user.id
        request.data['user'] = user
        return self.create(request, *args, **kwargs)


class StatusPK(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               generics.GenericAPIView):
    serializer_class = StatusSerializer

    def get_queryset(self):
        user = self.request.user.id
        self.request.data['user'] = user
        return Status.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TaskList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Task.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user.id
        request.data['user'] = user
        return self.create(request, *args, **kwargs)


class TaskPK(mixins.RetrieveModelMixin,
             mixins.UpdateModelMixin,
             mixins.DestroyModelMixin,
             generics.GenericAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user.id
        self.request.data['user'] = user
        return Task.objects.filter(user=user).all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
