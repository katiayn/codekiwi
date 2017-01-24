from django.test import TestCase
import factory
from django.urls import reverse

from codekiwi.kiwitesting.models import Product


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product


class ProductQuestionnaireCreateTestCase(TestCase):

    def test_vat_20_if_biscuit_coated_in_chocolate(self):
        product = ProductFactory()
        url = reverse('products:questionnaire', kwargs={'pk': product.pk})
        self.client.post(url, {
            'is_biscuit': True,
            'is_coated_in_chocolate': True
        })
        product.refresh_from_db()
        self.assertEqual(product.vat, 20)