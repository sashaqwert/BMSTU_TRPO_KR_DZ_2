from rest_framework import serializers


class loginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
