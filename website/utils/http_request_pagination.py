# coding: utf-8
from django.core.paginator import Paginator


def pagination_result(object_list, serializer, page=1, page_size=15):
    """
    分页返回数据
    :param object_list: 
    :param page: 
    :param page_size: 
    :param serializer：
    :return: 
    """
    assert not isinstance(object_list, list)
    pagination = Paginator(object_list, page_size)
    result = pagination.page(page)
    data = serializer(result, many=True).data
    page_count = pagination._num_pages
    return {
        "results": {
            'page': page,
            'page_size': page_size,
            'total_pages': page_count,
            'data': data
    }}
