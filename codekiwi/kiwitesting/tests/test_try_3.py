from django.test import SimpleTestCase

from codekiwi.kiwitesting.models import VATCalculator


class ProductQuestionnaireCreateTestCase(SimpleTestCase):

    def test_vat_20_if_biscuit_coated_in_chocolate(self):
        calc = VATCalculator()
        self.assertEqual(
            calc.calculate_vat(
                is_biscuit=True,
                is_coated_in_chocolate=True
            ), 20)