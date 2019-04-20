from .Serializer import CreateActivitySerializer, GetActivitySerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.views import APIView
import logging
logger = logging.getLogger('django')
from .models import Activity
from django.core.exceptions import ObjectDoesNotExist


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
