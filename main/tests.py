from django.test import TestCase
from django.urls import reverse
from .models import CV
from rest_framework.test import APITestCase


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


class CVAPITestCase(APITestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            firstname="API",
            lastname="User",
            bio="API bio",
            skills="Python, DRF",
            projects="API Project",
            contacts="api@example.com"
        )

    def test_list_cvs(self):
        url = reverse('cv-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_cv(self):
        url = reverse('cv-detail', args=[self.cv.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['firstname'], "API")

    def test_create_cv(self):
        url = reverse('cv-list')
        data = {
            "firstname": "New",
            "lastname": "CV",
            "bio": "New bio",
            "skills": "Django, REST",
            "projects": "New Project",
            "contacts": "new@example.com"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['firstname'], "New")

    def test_update_cv(self):
        url = reverse('cv-detail', args=[self.cv.pk])
        data = {"firstname": "Updated"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['firstname'], "Updated")

    def test_delete_cv(self):
        url = reverse('cv-detail', args=[self.cv.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
