from rest_framework import generics, status
from rest_framework.response import Response
from .models import ImagemUpload
from .serializers import ImagemUploadSerializer

def avaliar_imagem_com_modelo(caminho_da_imagem):
   
    print(f"--- Avaliando a imagem em: {caminho_da_imagem} ---")
    return "Resultado Fictício: A imagem parece ser de um cinto."


class UploadImagemView(generics.CreateAPIView):
    queryset = ImagemUpload.objects.all()
    serializer_class = ImagemUploadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        instancia_imagem = serializer.save()

        try:
            caminho_arquivo = instancia_imagem.imagem.path

            print("Verificações customizadas podem ser adicionadas aqui.")

            resultado_modelo = avaliar_imagem_com_modelo(caminho_arquivo)
            
            instancia_imagem.resultado = resultado_modelo
            instancia_imagem.save()

            serializer_atualizado = self.get_serializer(instancia_imagem)
            headers = self.get_success_headers(serializer_atualizado.data)
            return Response(serializer_atualizado.data, status=status.HTTP_201_CREATED, headers=headers)

        except Exception as e:
            instancia_imagem.delete()
            return Response(
                {"erro": f"Erro no processamento: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )