from django import forms

from codekiwi.kiwitesting.models import Product, ProductQuestionnaire


class ProductQuestionnaireForm(forms.ModelForm):

    class Meta:
        model = ProductQuestionnaire
        exclude = (
            'id',
            'product',
        )

    # for test_try_2
    def save(self, commit=True):
        instance = super().save(commit)
        is_biscuit = self.cleaned_data.get('is_biscuit')
        is_coated_in_chocolate = self.cleaned_data.get('is_coated_in_chocolate')
        if is_biscuit and is_coated_in_chocolate:
            product = Product.objects.get(id=instance.pk)
            product.set_vat_20()
        return instance