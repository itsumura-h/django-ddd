
from django.urls import path, include
# from .views.sample_user_views import SampleUserViews
from .views.ddd_sample_views import DDDSample
from .views.web_sample_views import WebSampleViews

from .views.test_views import TestViews

ddd_sample_urls = [
    path('', DDDSample.index),
]

# sample_urls = [
#     path('', SampleUserViews.index),
#     path('create/', SampleUserViews.create),
#     path('store/', SampleUserViews.store),
#     path('<int:id>/', SampleUserViews.show),
#     path('<int:id>/edit/', SampleUserViews.edit),
#     path('<int:id>/update/', SampleUserViews.update),
#     path('<int:id>/destroy/', SampleUserViews.destroy),
# ]

web_sample_urls = [
    path('', WebSampleViews.index),
    path('VueInstalled/', WebSampleViews.vue_installed),
    path('checkform/', WebSampleViews.checkform),
]


app_urls = [
    # path('sample/', include(sample_urls)),
    path('api/ddd_sample/', include(ddd_sample_urls)),
    path('WebSample/', include(web_sample_urls)),
]
