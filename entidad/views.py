from rest_framework import status
from rest_framework.views import APIView 
from rest_framework.response import Response
from entidad.models import EntidadModel
from entidad.serializers import EntidadSerializer 

"""
class EntidadApiView(APIView):
    def get(self, request):
        serializer = EntidadSerializer(EntidadModel.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def post(self, request): 
        #res = request.data.get('name')  
        serializer = EntidadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
"""

class EntidadApiView(APIView):

    def get(self, request):
        tipo_entidad_param = request.query_params.getlist('TipoEntidad')
        try:
            tipo_entidad_values = [int(value) for value in tipo_entidad_param]
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid TipoEntidad value'})

        if tipo_entidad_values:
            queryset = EntidadModel.objects.filter(TipoEntidad__in=tipo_entidad_values)
        else:
            queryset = EntidadModel.objects.all()

        serializer = EntidadSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = EntidadSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)

"""
class EntidadApiView(APIView):
    def get(self, request):
        tipo_entidad_param = request.query_params.getlist('TipoEntidad')
        try:
            tipo_entidad_values = [int(value) for value in tipo_entidad_param if value in ['0', '1', '2', '3']]
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'error': 'Invalid TipoEntidad value'})
        
        if tipo_entidad_values:
            queryset = EntidadModel.objects.filter(TipoEntidad__in=tipo_entidad_values)
        else:
            queryset = EntidadModel.objects.all()
            
        serializer = EntidadSerializer(queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = EntidadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
"""    
    
class EntidadApiViewDetail(APIView):
    def get_object(self, pk):
        try:
            return EntidadModel.objects.get(pk=pk)
        except EntidadModel.DoesNotExist:
            return None
    def get(self, request, id):
        post = self.get_object(id)
        serializer = EntidadSerializer(post)  
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    def put(self, request, id):
        post = self.get_object(id)
        if(post==None):
            return Response(status=status.HTTP_200_OK, data={ 'error': 'Not found data'})
        serializer = EntidadSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        post = self.get_object(id)
        post.delete()
        response = { 'deleted': True }
        return Response(status=status.HTTP_204_NO_CONTENT, data=response)

