import email
from itertools import product
from math import prod
from os import stat
import re
from unicodedata import name
from django.shortcuts import render
from Api import serializers

# Create your views here.
from Api.models import User, Product
from Api.serializers import UserSerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.hashers import check_password


@api_view(["POST"])
def register(request):

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.filter(email=request.data.get("email"))
        if not user:
            user = User.objects.filter(email=serializer.data["email"])
            refresh = RefreshToken.for_user(user[0])
            return Response(
                {
                    "accessToken": str(refresh.access_token),
                    "refreshToken": str(refresh),
                    "id": serializer.data["id"],
                    "email": serializer.data["email"],
                    "name": serializer.data["name"],
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"message": "Email already exists!"}, status=status.HTTP_400_BAD_REQUEST
            )
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    serializer = UserSerializer.validate_login(data=request.data)
    user = User.objects.filter(email=request.data["email"])
    if len(user) and check_password(request.data["password"], user[0].password):
        id = user[0].id
        refresh = RefreshToken.for_user(user[0])
        return Response(
            {
                "accessToken": str(refresh.access_token),
                "refreshToken": str(refresh),
                "id": user[0].id,
                "email": user[0].email,
                "name": user[0].name,
            },
            status=status.HTTP_200_OK,
        )
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


def get_pagination_data(page):
    if page and page.isnumeric():
        page = int(page)
    else:
        page = 1
    limit = page * 10
    offset = limit - 10

    return limit, offset, page


@api_view(["POST", "GET"])
def products_controller(request):
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        seller = request.query_params.get("seller")
        limit, offset, page = get_pagination_data(request.query_params.get("page"))

        if seller:
            products = (
                Product.objects.all()
                .order_by("price")
                .filter(seller=seller)[offset:limit]
            )
        else:
            products = Product.objects.all().order_by("price")[offset:limit]
        serializer = ProductSerializer(products, many=True)
        return Response(
            {"data": serializer.data, "page": page}, status=status.HTTP_200_OK
        )
