from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.cbv import SnippetList, SnippetDetail, UserList, UserDetail


urlpatterns = [
    url(r'^$', SnippetList.as_view(), name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', SnippetDetail.as_view(), name='snippet_detail'),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)

