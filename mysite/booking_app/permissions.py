from rest_framework import permissions
from setuptools.command.build_ext import if_dl
from urllib3 import request


class CheckCreateHotel(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'ownerUser'


class CheckHotelOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CreateReview(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.user_role == 'simpleUser'
