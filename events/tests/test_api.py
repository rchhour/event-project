from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class EventSerializerTestCase(APITestCase):

	def event_creation_test(self):
		payload = {
			"name": "jazz",
			"description": "instruments",	
			"startDate": "2021-05-06",
			"endDate": "2021-10-",
		}

		response = self.client.post(reverse("event-create"), payload)
		self.assertEqual(status.HTTP_201_CREATED, response.status_code)      

    