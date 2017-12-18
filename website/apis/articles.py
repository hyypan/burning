# import the logging library
import logging

# Get an instance of a logger
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from website.models import *
from website import read_serializer
from website.utils.http_request_pagination import pagination_result

logger = logging.getLogger(__name__)


@api_view(['GET', 'POST', 'DELETED', 'PATCH'])
@permission_classes((AllowAny, ))
def articles(request):
    if request.method == 'GET':
        articles_list = Articles.objects.all()
        print 1111
        data = pagination_result(articles_list, read_serializer.ArticlesSerializer)
        return Response(data)
