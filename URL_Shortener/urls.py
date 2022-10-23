from django.urls import path

from .views import *

urlpatterns = [
    # path('example/', example_view),
    path('example/<slug:name>', example_view),
    path('task/', task_view),
    path('shorten/', shorten_url),
    path('redirect/<slug:name>', redirect_url),
    path('all-analytics/',all_analytics),
    path('all-analytics/<slug:name>',deep_analytics)
]