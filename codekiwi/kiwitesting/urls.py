from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^(?P<pk>\d+)/questionnaire/$',
        views.ProductQuestionnaire.as_view(),
        name='questionnaire'
    )
]
