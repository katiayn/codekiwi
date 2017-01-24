from django.views.generic.edit import CreateView

from codekiwi.kiwitesting.forms import ProductQuestionnaireForm
from codekiwi.kiwitesting.models import Product


class ProductQuestionnaire(CreateView):

    form_class = ProductQuestionnaireForm
    model = Product
    success_url = '/admin/'

    # for test_try_1
    # def form_valid(self, form):
    #     self.instance = form.save(commit=False)
    #     object = self.get_object()
    #     if self.instance.is_biscuit and self.instance.is_coated_in_chocolate:
    #         object.set_vat_20()
    #     return super().form_valid(form)
