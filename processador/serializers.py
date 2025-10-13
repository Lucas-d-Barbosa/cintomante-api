from rest_framework import serializers
from .models import ImagemUpload

class ImagemUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagemUpload
        fields = ['id', 'imagem', 'resultado', 'enviado_em']
        read_only_fields = ['resultado', 'enviado_em']