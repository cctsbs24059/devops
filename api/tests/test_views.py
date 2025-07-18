from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        # 200 =< 300 successful
        # 400 =< 500 unexpected behaviour
        # 500 something wrong on the server side (bug, disconnection on infrastructure)
        url = reverse('api:books')
        response =  self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['hello'] == 'django'

class HealthViewTest(APITestCase):
    def test_response_is_correct(self):
        # 200 =< 300 successful
        # 400 =< 500 unexpected behaviour
        # 500 something wrong on the server side (bug, disconnection on infrastructure)
        url = reverse('api:health')
        response =  self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'