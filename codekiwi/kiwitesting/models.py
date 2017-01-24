from django.db import models
from django.utils.translation import ugettext as _


class Employee(models.Model):
    last_name = models.CharField(
        max_length=255, verbose_name='Surname', blank=True
    )
    first_name = models.CharField(
        max_length=255, verbose_name='Name', blank=True
    )
    job = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Job Position'
    )


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name', blank=True)
    price = models.DecimalField(
        _('Price'),
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True
    )
    vat = models.IntegerField(_('Vat'), blank=True, null=True)

    def set_vat_20(self):
        self.vat = 20
        self.save()


class ProductQuestionnaire(models.Model):
    product = models.ForeignKey(
        Product, blank=True, null=True, verbose_name='Product'
    )
    is_biscuit = models.BooleanField(
        default=False, verbose_name='Biscuit?'
    )
    is_coated_in_chocolate = models.BooleanField(
        default=False, verbose_name='Coated in Chocolate?'
    )


class VATCalculator(object):

    def calculate_vat(self, **kwargs):
        is_biscuit = kwargs['is_biscuit']
        is_coated_in_chocolate = kwargs['is_coated_in_chocolate']
        if is_biscuit and is_coated_in_chocolate:
            return 20