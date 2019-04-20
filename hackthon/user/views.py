from django.shortcuts import render

# Create your views here.
from .Serializer import CreateUser
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import logging
logger = logging.getLogger('django')
from .models import User
import requests


# Create your views here.
class UserView(APIView):
    def post(self, request):

        try:
            data = JSONParser().parse(request)
            #print(data)
            code = data['code']
            #print(code)
            # openid = code_convert(code)
            openid = '123'
            #print(data)
            del data['code']
            #print(data)
            data['open_id'] = openid
            #print(data)
            serializer = CreateUser(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'status': 200, 'msg': '添加成功！'})
            else:
                return JsonResponse({'status': 403, 'msg': '载荷错误！'})
        except Exception as e:
            return JsonResponse({'status': 500, 'msg': str(e)})


def code_convert(code):
    js_code = code
    appid = 'wx9f3b544a8b2be233'
    secret = 'ce7674d0b0ad90e189c75fc1b14'
    requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx9f3b544a8b2be233&secret=5a7f3ce7674d0b0ad90e189c75fc1b14&js_code=' + js_code + '&grant_type=authorization_code'
    print(requestString)
    r = requests.get(requestString)

    r = r.json()
    print(r)
    openid = r['openid']
    return openid
