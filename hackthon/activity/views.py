from .Serializer import CreateActivitySerializer, GetActivitySerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import logging
logger = logging.getLogger('django')
from .models import Activity


# Create your views here.
class ActivityView(APIView):
    def post(self, request, format=None):
        try:
            # data = JSONParser().parse(request)
            # logger.info(data)
            # serializer = CreateActivitySerializer(data=data)
            # return JsonResponse(serializer.errors, status=200)
            return JsonResponse({'xx': "大家觉得"})
        except Exception as e:
            logger.info(e)
            # return JsonResponse(serializer.errors, status=500)
            return JsonResponse({'xx': "456"})

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
