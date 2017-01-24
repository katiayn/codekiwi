from django.test import TestCase
import factory

from codekiwi.kiwitesting.models import Product
from codekiwi.kiwitesting.forms import ProductQuestionnaireForm


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product


class ProductQuestionnaireCreateTestCase(TestCase):

    def test_vat_20_if_biscuit_coated_in_chocolate(self):
        product = ProductFactory()
        form = ProductQuestionnaireForm(data={
            'is_biscuit': True,
            'is_coated_in_chocolate': True,
        })
        self.assertTrue(form.is_valid())
        form.save()
        product.refresh_from_db()
        self.assertEqual(product.vat, 20)