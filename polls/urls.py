from django.conf.urls import url, include
from rest_framework import routers
#from .polls import views

from . import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'Choices', views.ChoiceViewSet)

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^api/$', views.questionss_api, name='questions_api'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
