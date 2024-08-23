from rest_framework import serializers


class DmSerializer(serializers.Serializer):
    distro = serializers.CharField(max_length=50)
    version = serializers.CharField(max_length=10)
    packages = serializers.ListField(
        child=serializers.CharField(max_length=100))
