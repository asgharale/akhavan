from rest_framework.serializers import ModelSerializer
from .models import Image, Video, File


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'