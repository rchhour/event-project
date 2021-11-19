from django.test import TestCase
from events.models import Event

class EventModelTestCase(TestCase):

	def test_create_event(self):
		ev1 = Event.objects.create(name="violin",description="groupe de musique",startDate="2021-05-10",endDate="2021-10-10")		
		self.assertIsInstance(ev1,Event)
		self.assertEqual(str(ev1),'violin')


    