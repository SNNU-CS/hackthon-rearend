import requests
from user.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Activity, UserActivity
from .Serializer import CreateActivitySerializer, GetActivitySerializer, ActivitySerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.views import APIView
import logging
logger = logging.getLogger('django')


# Create your views here.
class ActivityView(APIView):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = CreateActivitySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'status': 200, 'msg': '添加成功!'})
            else:
                return JsonResponse({'status': 403, 'msg': '载荷错误!'})
        except Exception as e:
            logger.info(e)
            return JsonResponse({'status': 500, 'msg': str(e)})

    def get(self, request, pk):
        try:
            data = Activity.objects.get(pk=pk)
            serializer = GetActivitySerializer(data, many=False)
            return JsonResponse({
                'status': 200,
                'msg': '查询成功',
                'data': serializer.data
            })
        except ObjectDoesNotExist:
            return JsonResponse({'status': 200, 'msg': "不存在的id", 'data': None})
        except Exception as e:
            return JsonResponse({'status': 500, 'msg': str(e), 'data': None})


class ActivityListView(APIView):
    def get(self, request):
        try:
            data = Activity.objects.all()
            serializer = GetActivitySerializer(data, many=True)
            return JsonResponse({
                'status': 200,
                'msg': '查询成功',
                'data': serializer.data
            })
        except Exception as e:
            return JsonResponse({'status': 500, 'msg': str(e), 'data': None})


class UserActivityView(APIView):
    def get(self, request, id):
        try:
            open_id = code_convert(id)
            # open_id = 'oBsDr4rGaO9V8UcJqBsyL571h4oU'
            user_id = User.objects.get(open_id=open_id).id
            ls = []
            for e in UserActivity.objects.filter(user_id=user_id):
                ls.append(e.activity_id)
            data = Activity.objects.filter(id__in=ls)
            serializer = ActivitySerializer(data, many=True)
            return JsonResponse({
                'status': 200,
                'msg': '查询成功',
                'data': serializer.data
            })
        except ObjectDoesNotExist:
            return JsonResponse({'status': 200, 'msg': "不存在的id", 'data': None})
        except Exception as e:
            return JsonResponse({'status': 500, 'msg': str(e), 'data': None})

    def post(self, request, id):
        try:
            open_id = code_convert(id)
            # open_id = 'oBsDr4idTS54BBl9IQ0PoO3IfL5w'
            user_id = User.objects.get(open_id=open_id).id
            activity_id = request.data['activity_id']
            check = UserActivity.objects.filter(activity_id=activity_id,
                                                user_id=user_id).count()
            if check > 0:
                return JsonResponse({
                    'status': 200,
                    'msg': '该用户已参与此活动!',
                })
            activity = Activity.objects.get(pk=activity_id)
            activity.number_now += 1
            activity.save()
            UserActivity.objects.create(activity_id=activity_id,
                                        user_id=user_id,
                                        user_class='A')
            return JsonResponse({
                'status': 200,
                'msg': '添加成功',
            })
        except ObjectDoesNotExist:
            return JsonResponse({'status': 200, 'msg': "不存在的id"})
        except Exception as e:
            return JsonResponse({'status': 500, 'msg': str(e)})


def code_convert(code):
    js_code = code
    appid = 'wx9f3b544a8b2be233'
    secret = 'ce7674d0b0ad90e189c75fc1b14'
    requestString = 'https://api.weixin.qq.com/sns/jscode2session?appid=wx9f3b544a8b2be233&secret=5a7f3ce7674d0b0ad90e189c75fc1b14&js_code=' + js_code + '&grant_type=authorization_code'
    r = requests.get(requestString)
    r = r.json()
    openid = r['openid']
    return openid
