from celerybeat_status.views import PeriodicTasksStatusListView
import django


if django.get_version() < (4, 0, 0):
    from django.conf.urls import url

    urlpatterns = [
        url(r'^periodic-tasks/$', PeriodicTasksStatusListView.as_view(),
            name='periodic-tasks-status'),
    ]
else:
    from django.urls import re_path

    urlpatterns = [
        re_path('^periodic-tasks/$', PeriodicTasksStatusListView.as_view(),
            name='periodic-tasks-status'),
    ]
