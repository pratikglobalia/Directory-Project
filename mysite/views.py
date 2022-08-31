from rest_framework.views import APIView
from .models import *
from .serializers import DirectorySerializer, FileSerializer
from rest_framework.response import Response

# Create your views here.
class DirectoryView(APIView):
    def get(self, requesst, format=None, pk=None):
        if pk is not None:
            fpk = File.objects.filter(directory=pk)
            dpk = Directory.objects.filter(directory=pk)
            fpk_serializer = FileSerializer(fpk, many=True)
            dpk_serializer = DirectorySerializer(dpk, many=True)
            return Response({
                'file_data' : fpk_serializer.data,
                'directory_data' : dpk_serializer.data
            })
        fdata = File.objects.filter(directory__isnull=True)
        ddata = Directory.objects.filter(directory__isnull=True)
        file_serializer = FileSerializer(fdata, many=True)
        directory_serializer = DirectorySerializer(ddata, many=True)
        return Response({
            'file_data' : file_serializer.data,
            'directory_data' : directory_serializer.data
        })
    
    
    def post(self, request, format=None):          
        file_serializer = FileSerializer(data=request.data)
        directory_serializer = DirectorySerializer(data=request.data)
        serializer = {
            'fdata':file_serializer,
            'ddata':directory_serializer
            }
        if file_serializer.is_valid(raise_exception=True):
            file_serializer.save()
            
        if directory_serializer.is_valid(raise_exception=True):
            directory_serializer.save()
            
        data = {
            "file_serializer":file_serializer.data,
            "directory_serializer":directory_serializer.data
            }
            
        return Response(data)
  