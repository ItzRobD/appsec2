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
        self.assertEqual(response.context.get('director', None), payload)

	def test_csrf(self):
		params = {'username': 'zerocool', 'amount' : '100'}
		response = self.csrf_client.post('/gift/2', params)
		self.assertEqual(response.status_code, 403)

	def test_sql(self):
		self.client.login(username='admin', password='adminpassword')
		with open('part 1/attack.gftcrd') as f:
			params = {'card_supplied': 'True', 'card_data': f}
			response = self.client.post('/use.html', params)
		self.assertEqual(response.context.get('card_found', None), None)
