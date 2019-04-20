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
