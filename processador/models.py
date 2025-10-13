import os
from django.db import models
from uuid import uuid4

def upload_para_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}.{ext}'
    return os.path.join('imagens/', filename)

class ImagemUpload(models.Model):
    imagem = models.ImageField(upload_to=upload_para_path)
    resultado = models.CharField(max_length=255, blank=True, null=True)
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Imagem {self.id} enviada em {self.enviado_em.strftime('%d/%m/%Y %H:%M')}"