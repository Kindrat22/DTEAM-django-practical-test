from django.test import TestCase
from django.urls import reverse
from .models import CV


class CVViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CV.objects.create(
            firstname="Test",
            lastname="User",
            bio="Test bio",
            skills="Python, Django",
            projects="Test Project",
            contacts="test@example.com"
        )

    def test_cv_list_view(self):
        response = self.client.get(reverse('cv_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User")

    def test_cv_detail_view(self):
        cv = CV.objects.first()
        response = self.client.get(reverse('cv_detail', args=[cv.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test bio")
