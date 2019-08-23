
from django.urls import path, include
from .views.sample_views import SampleViews

sample_urls = [
    path('', SampleViews.index),
    path('create/', SampleViews.create),
    path('store/', SampleViews.store),
    path('<int:id>/', SampleViews.show),
    path('<int:id>/edit/', SampleViews.edit),
    path('<int:id>/update/', SampleViews.update),
    path('<int:id>/destroy/', SampleViews.destroy),
]

app_urls = [
    path('sample/', include(sample_urls)),
]
