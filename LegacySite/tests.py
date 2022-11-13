from django.test import TestCase, Client

# Create your tests here.
class AppSec2Tests(TestCase):
	fixtures = ['fixture.json']

	def setUp(self):
		self.client = Client()
		self.csrf_client = Client(enforce_csrf_checks=True)

	def test_xss(self):
		payload = "<script>alert('This is an XSS vulnerability')</script>"
		params = {'director': payload}
		response = self.client.get('/gift.html', params)

