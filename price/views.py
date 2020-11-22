from django.shortcuts import render

from price.models import Product
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import authentication

from . serializers import PKSerializer

from . switch import extract_to_update


class ExtractProductURL(UpdateAPIView):
    serializer_class = PKSerializer

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        serializer = self.get_serializer(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        response = extract_to_update(pk=request.data['pk'])
        return Response(response)
