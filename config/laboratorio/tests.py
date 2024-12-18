from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre="Laboratorio 1", ciudad="Ciudad 1", pais="País 1")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/laboratorio/1/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('laboratorio:detalle_laboratorio', args=[1]))
        self.assertEqual(response.status_code, 200)


class LaboratorioTemplateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Laboratorio.objects.create(nombre="Laboratorio 1", ciudad="Ciudad 1", pais="País 1")

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('laboratorio:detalle_laboratorio', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/detalle_laboratorio.html')

    def test_view_html_content(self):
        response = self.client.get(reverse('laboratorio:detalle_laboratorio', args=[1]))
        self.assertContains(response, 'Laboratorio 1')
        self.assertContains(response, 'Ciudad 1')
        self.assertContains(response, 'País 1')


