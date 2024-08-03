from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import Documento
from .serializers import DocumentoSerializer

from docx2pdf import convert 

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import FileResponse
import pypandoc
import os

class DocumentoListCreateView(generics.ListCreateAPIView):
    serializer_class = DocumentoSerializer

    def get_queryset(self):
        return Documento.objects.all().order_by('-fecha')[:6]

class DocumentoUploadView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = DocumentoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Documento subido exitosamente.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DocumentoVistaPDF(APIView):
    
    def get(self, request, documento_id, format=None):
        documento = get_object_or_404(Documento, id=documento_id)
        input_path = documento.archivo.path
        output_path = os.path.join(settings.MEDIA_ROOT, 'archivo', f'{documento_id}.pdf')

        if not input_path.lower().endswith('.docx'):
            return Response({'error': 'El archivo no es un archivo DOCX.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            convert(input_path, output_path)
        except Exception as e:
            return Response({'error': f'Error al convertir el archivo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        if not os.path.exists(output_path):
            return Response({'error': 'El archivo PDF no se pudo generar.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        response = FileResponse(open(output_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="documento.pdf"'
        return response
    
class DocumentoDescarga(APIView):

    def get(self, request, documento_id, format=None):
        documento = get_object_or_404(Documento, id=documento_id)
        input_path = documento.archivo.path

        if not input_path.lower().endswith('.docx'):
            return Response({'error': 'El archivo no es un archivo DOCX.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not os.path.exists(input_path):
            return Response({'error': 'El archivo DOC no se pudo encontrar.'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            response = FileResponse(open(input_path, 'rb'), content_type='application/msword')
            response['Content-Disposition'] = f'attachment; filename="{documento_id}.docx"'
            return response
        except Exception as e:
            return Response({'error': f'Error al servir el archivo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)