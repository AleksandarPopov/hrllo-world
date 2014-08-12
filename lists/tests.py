from django.test import TestCase

class SmokeTest(TestCase):
	def test_bad_maths(self):
		self.asertEqual(1+1,3)
# Create your tests here.
