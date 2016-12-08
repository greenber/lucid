from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^addStory/$', views.addStory, name='addStory'),

    url(r'^(?P<story_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<story_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<story_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^(?P<story_id>[0-9]+)/playGame/$', views.playGame, name='playGame'),

    url(r'^(?P<story_id>[0-9]+)/delPoint/$', views.delPoint, name='delPoint'),
]