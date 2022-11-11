from django.core.cache import cache
from django.test import TestCase, Client
import unittest
from django.http import HttpResponse
from django.test.utils import setup_test_environment, teardown_test_environment
from django.urls import reverse

teardown_test_environment()
setup_test_environment()

# Create your tests here.
class AppSecTests(TestCase):
    def setup(self):
        self.client = Client()

    def test_xss(self):
        cache.clear()
        payload = "<script>alert('This is an XSS vulnerability')</script>"
        #payload = 'this is a test'
        params = {'director': payload}
        response = self.client.get('/gift.html', params)

        print(f"Response: {response}")
        print(f'Response Code: {response.status_code}')
        #print(f"Response content params:{response.content_params}")
        #print(f"Response content type:{response.content_type}")
        print(f"Response content: {response.content}")


        #self.assertEqual(response.status_code, 200)

        #self.assertEqual(response.context['director'], payload)
