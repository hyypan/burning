# coding: utf-8

from rest_framework import serializers


class ArticlesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    is_deleted = serializers.BooleanField()
    create_time = serializers.DateTimeField()
    last_update = serializers.DateTimeField()
    content = serializers.CharField(max_length=5000)
    title = serializers.CharField(max_length=256)
    belongs_id = serializers.IntegerField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
