from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from .models import RequestLog
from .middleware import RequestLogMiddleware

class RequestLogMiddlewareTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = RequestLogMiddleware()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')

    def test_log_created_for_request(self):
        request = self.factory.get('/test-path/?foo=bar')
        request.user = self.user
        self.middleware.process_request(request)
        log = RequestLog.objects.last()
        self.assertIsNotNone(log)
        self.assertEqual(log.path, '/test-path/')
        self.assertEqual(log.method, 'GET')
        self.assertEqual(log.query_string, 'foo=bar')
        self.assertEqual(log.user, self.user)
