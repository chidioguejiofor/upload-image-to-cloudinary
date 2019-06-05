from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, JSONParser

import cloudinary.uploader

class UploadView(APIView):
    parser_classes = (
        MultiPartParser,
        JSONParser,
    )

    @staticmethod
    def post(request):
        file = request.data.get('picture')
        upload_data = cloudinary.uploader.upload(file)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)
