from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from django.conf import settings
import json


def home(request):
    dataSensor = dataSensor.objects.all()
    sensors_names = list()

    for sensors in dataSensor:
        sensors_names.append(sensors.name)

    response_html = '<br>'.join(sensors_names)

    return HttpResponse(response_html)


@api_view(["POST"])
def postInfo(Data):
    try:
        body=json.loads(Data.body)
        output =str(body)
        return JsonResponse(output,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def Info(request):
    pass
