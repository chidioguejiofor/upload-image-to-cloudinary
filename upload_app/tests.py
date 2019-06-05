import pytest
from unittest.mock import Mock
from rest_framework.test import APIClient
import cloudinary.uploader
import os
from tempfile import TemporaryFile

django_client = APIClient()
class TestUploadImage():
    def test_upload_image_to_cloudinary_succeeds(
            self):

        cloudinary_mock_response = {
            'public_id': 'public-id',
            'secure_url': 'http://hello.com/here',
        }
        cloudinary.uploader.upload = Mock(
            side_effect=lambda *args: cloudinary_mock_response)


        with TemporaryFile() as temp_image_obj:
            for line in open(os.path.dirname(__file__) + '/mock-image.png', 'rb'):
                temp_image_obj.write(line)

            response = django_client.post(
                '/api/upload-image',
                {'picture': temp_image_obj},
                format="multipart",
            )

            response_data = response.data

            assert response.status_code == 201
            assert response_data['status'] == 'success'
            assert response_data['data'] == cloudinary_mock_response
            assert cloudinary.uploader.upload.called

