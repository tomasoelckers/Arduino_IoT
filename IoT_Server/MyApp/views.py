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
from .models import dataSensor


def home(request):
    return HttpResponse("Hello IoT!!!")

def Info(request):
    objects = dataSensor.objects.all()
    return render(request, 'info_v2.html', {'dataSensor': objects})


@api_view(["POST"])
def postInfo(Data):
    try:
        body=json.loads(Data.body)
        for i in body:
            dataSensor.objects.filter(name=i).update(value=body[i])
        return JsonResponse(body,safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
