# coding: utf-8
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from website.models import *


class BelongsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField()
    create_time = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    comments_count = serializers.SerializerMethodField()
    views = serializers.IntegerField()
    loves = serializers.IntegerField()

    def get_comments_count(self, obj):
        return Comments.objects.filter(is_deleted=False, belongs_id=obj.id).count()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ArticlesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField()
    create_time = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    content = serializers.CharField(max_length=5000)
    title = serializers.CharField(max_length=256)
    belongs_id = serializers.IntegerField()
    belongs = serializers.SerializerMethodField()

    def get_belongs(self, obj):
        try:
            belongs = Belongs.objects.get(is_deleted=False, id=obj.belongs_id)
            return BelongsSerializer(belongs).data
        except ObjectDoesNotExist:
            pass

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
