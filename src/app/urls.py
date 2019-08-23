
from django.urls import path, include
from .views.sample_user_views import SampleUserViews

sample_urls = [
    path('', SampleUserViews.index),
    path('create/', SampleUserViews.create),
    path('store/', SampleUserViews.store),
    path('<int:id>/', SampleUserViews.show),
    path('<int:id>/edit/', SampleUserViews.edit),
    path('<int:id>/update/', SampleUserViews.update),
    path('<int:id>/destroy/', SampleUserViews.destroy),
]

app_urls = [
    path('sample/', include(sample_urls)),
]
